"""Read-only PE header inventory. Does not execute or decompile the input."""
import argparse
import hashlib
import json
from pathlib import Path
import struct


def inspect(path):
    path = Path(path)
    size = path.stat().st_size
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)

        def read_at(offset, length):
            if offset < 0 or offset + length > size:
                raise ValueError('Truncated PE header or out-of-range offset')
            stream.seek(offset)
            data = stream.read(length)
            if len(data) != length:
                raise ValueError('File changed or was truncated while reading')
            return data

        dos = read_at(0, 64)
        if dos[:2] != b'MZ':
            raise ValueError('Not a DOS/PE executable: missing MZ signature')
        pe_offset = struct.unpack_from('<I', dos, 60)[0]
        if pe_offset < 64:
            raise ValueError('Invalid PE header offset')
        header = read_at(pe_offset, 24)
        if header[:4] != b'PE\0\0':
            raise ValueError('Missing PE signature')
        machine, count, timestamp, _, _, optional_size, flags = struct.unpack_from('<HHIIIHH', header, 4)
        if count == 0 or count > 96:
            raise ValueError('Unsupported or invalid section count')
        optional = read_at(pe_offset + 24, optional_size)
        if len(optional) < 2:
            raise ValueError('Missing optional executable header')
        magic = struct.unpack_from('<H', optional)[0]
        if magic not in (0x10B, 0x20B):
            raise ValueError('Unsupported optional header format')
        minimum = 96 if magic == 0x10B else 112
        if len(optional) < minimum:
            raise ValueError('Truncated optional executable header')
        entry = struct.unpack_from('<I', optional, 16)[0]
        base = struct.unpack_from('<I' if magic == 0x10B else '<Q', optional, 28 if magic == 0x10B else 24)[0]
        sections = []
        for index in range(count):
            section = read_at(pe_offset + 24 + optional_size + index * 40, 40)
            virtual_size, rva, raw_size, raw_offset = struct.unpack_from('<IIII', section, 8)
            if raw_size and raw_offset + raw_size > size:
                raise ValueError('Section raw data extends beyond file')
            sections.append({
                'name': section[:8].rstrip(b'\0').decode('ascii', errors='replace'),
                'virtual_size': virtual_size, 'rva': hex(rva),
                'raw_size': raw_size, 'raw_offset': raw_offset,
                'characteristics': hex(struct.unpack_from('<I', section, 36)[0]),
            })
    return {
        'schema_version': 1, 'sha256': digest.hexdigest(), 'size_bytes': size,
        'machine': hex(machine),
        'architecture': {0x8664: 'x86_64', 0x14C: 'x86', 0xAA64: 'ARM64'}.get(machine, 'unknown'),
        'format': 'PE32+' if magic == 0x20B else 'PE32',
        'coff_timestamp_raw': timestamp,
        'image_base': hex(base), 'entry_point_rva': hex(entry),
        'characteristics': hex(flags), 'sections': sections,
        'limitations': ['Header inventory only; no imports, decompilation, packing detection or runtime validation.'],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('executable', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.output and args.output.resolve() == args.executable.resolve():
        parser.error('Output must not overwrite the input executable')
    try:
        report = inspect(args.executable)
    except (OSError, ValueError, struct.error) as error:
        parser.error(str(error))
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding='utf-8')
    else:
        print(rendered, end='')


if __name__ == '__main__':
    main()
