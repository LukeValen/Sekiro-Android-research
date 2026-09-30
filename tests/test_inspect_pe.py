"""Synthetic inputs only: no game files required."""
import hashlib
from pathlib import Path
import struct
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from inspect_pe import inspect


def fixture():
    data = bytearray(512)
    data[:2] = b'MZ'
    struct.pack_into('<I', data, 60, 64)
    data[64:68] = b'PE\0\0'
    struct.pack_into('<HHIIIHH', data, 68, 0x8664, 1, 0, 0, 0, 240, 0x22)
    struct.pack_into('<H', data, 88, 0x20B)
    struct.pack_into('<I', data, 104, 0x1000)
    struct.pack_into('<Q', data, 112, 0x140000000)
    data[328:336] = b'.text\0\0\0'
    struct.pack_into('<IIII', data, 336, 16, 0x1000, 16, 496)
    return data


class InspectTest(unittest.TestCase):
    def run_input(self, data):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'synthetic.exe'
            path.write_bytes(data)
            report = inspect(path)
            self.assertEqual(path.read_bytes(), data)
            return report

    def test_pe64_inventory_and_no_modification(self):
        data = fixture()
        report = self.run_input(data)
        self.assertEqual(report['architecture'], 'x86_64')
        self.assertEqual(report['format'], 'PE32+')
        self.assertEqual(report['sha256'], hashlib.sha256(data).hexdigest())
        self.assertEqual(report['image_base'], '0x140000000')
        self.assertEqual(report['sections'][0]['name'], '.text')

    def test_reject_truncated_file(self):
        with self.assertRaises(ValueError):
            self.run_input(fixture()[:100])

    def test_reject_bad_signature(self):
        data = fixture()
        data[64] = 0
        with self.assertRaises(ValueError):
            self.run_input(data)

    def test_reject_out_of_range_section(self):
        data = fixture()
        struct.pack_into('<I', data, 348, 500)
        with self.assertRaises(ValueError):
            self.run_input(data)


if __name__ == '__main__':
    unittest.main()
