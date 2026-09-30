# Sekiro Android Research

Research into the feasibility of a native ARM64 Android port of Sekiro, using the PC version as a reference. Project author: LukeValen.

**Status: initial investigation. This repository has no APK or reconstructed engine, and no game executable has been analyzed yet.**

## Goal and technical limitations

A decompiler helps investigate an executable, but its pseudocode does not automatically recover the original C++ project or an Android build. A native port would require reconstructing and validating the logic and adapting graphics, platform APIs, input, audio, memory, threading, file access, and dependencies.

The goal remains a native port. Wine with Box64/FEX and DXVK may provide a behavior and performance reference, but that approach runs the existing executable through compatibility and translation layers.

## First step in Termux

Use your own PC installation as local input. The inspector does not execute or modify the game and uses only the Python standard library.

```sh
pkg install python git
termux-setup-storage
python tools/inspect_pe.py '/storage/emulated/0/Download/Sekiro/sekiro.exe' --output analysis-local/executable.json
```

The path is an example; adjust it to your folder. The report includes SHA-256, PE format, architecture, and sections. It does not contain decompiled functions or a dependency list. Later, inspect imports using `llvm-readobj --coff-imports` with an LLVM version available in your environment, or Ghidra's import view.

Read the [research](docs/RESEARCH.md), [roadmap](docs/ROADMAP.md), and [repository instructions](docs/GITHUB.md).

## Local files

Keep executables, DLLs, game assets, saves, dumps, Ghidra projects, and decompilation output out of commits. This repository contains documentation and original tools; users supply their own game files locally.

## Tool verification

```sh
python -m unittest discover -s tests -v
```

These tests verify the inspector against synthetic files. They do not establish Sekiro compatibility or port feasibility.
