# Technical research — 2026-09-30

## Findings

The public search performed did not identify a complete, recompilable Sekiro decompilation or an open native Android port. This is a limited search result, not proof that none exists. No executable has been supplied or analyzed; the architecture, imports, and middleware used by the user's copy still need verification.

## Tools and their actual scope

| Tool | Purpose | Limitation for this project |
| --- | --- | --- |
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | Disassembly, decompilation, and executable investigation | Does not automatically turn pseudocode into a portable engine |
| [UXM](https://github.com/JKAnderson/UXM) | Unpacks game archives and adjusts loose-file loading for Sekiro | Does not decompile the engine; patches are unnecessary at this stage |
| [SoulsFormats](https://github.com/JKAnderson/SoulsFormats) | .NET library for reading and writing FromSoftware formats | Reading formats does not implement rendering, gameplay, or animation |
| [DSLuaDecompiler](https://github.com/katalash/DSLuaDecompiler) | Decompiles Lua/HavokScript AI and behavior scripts | Handles scripts, not the entire game executable |
| [Box64](https://github.com/ptitSeb/box64) | Runs Linux x86-64 programs on other architectures, with support for use with Wine | Requires environment integration; does not generate the game's source code |
| [FEX](https://github.com/FEX-Emu/FEX) | Emulates x86/x86-64 applications on ARM64 Linux | Is neither a Sekiro APK nor a complete Android solution by itself |
| [DXVK](https://github.com/doitsujin/dxvk) | Translates Direct3D 8/9/10/11 to Vulkan alongside Wine | Requires an appropriate Vulkan driver and features; does not replace CPU translation |

## Three different approaches

1. **Compatibility:** preserve the executable and translate CPU instructions and APIs. This is a smaller-scope approach to attempting to run the game, but does not fulfill the native-port goal by itself.
2. **Native reconstruction:** study functions and formats, write portable implementations, and validate them module by module. This is the project's goal and involves much greater scope.
3. **Static recompilation:** translate the binary into another compilable representation. Indirect calls, ABI, libraries, OS APIs, and graphics still require solutions. The search did not identify a tool demonstrated to do this end to end for Sekiro.

These conclusions are technical assessments based on documented tool capabilities, not game test results.

## Why decompilation alone is insufficient

An executable does not automatically provide original names, types, project organization, build settings, or library sources. Optimization merges or removes abstractions. Beyond reconstructed logic, investigation must cover calling conventions, object layouts, pointers and callbacks, synchronization, SIMD, shaders, dependencies, and file formats.

Having assets or a working viewer does not establish a functioning engine. Do not estimate FPS or a delivery date without execution evidence.

## Working from Android

Termux is sufficient to start with Git, Python, hashes, and small static reports. Full Ghidra analysis of a large executable and dynamic validation are more practical on a computer or suitable remote environment. A complete phone-only Ghidra workflow for this game has not been verified. Android builds can run in CI once sufficient native code exists; adding a workflow now would not produce the game.

## Evidence needed before selecting an architecture

- SHA-256 and the executable's exact edition/build.
- Format, architecture, sections, normal imports, and delay-loaded imports.
- Libraries and components actually used, including dynamic loading.
- Graphics features observed in logs or captures; published requirements alone are insufficient.
- Target device, Android version, RAM, GPU, and verified Vulkan driver.
- A small function whose behavior can be compared against an original implementation.

The URLs above were consulted as primary sources. None of these tools has been incorporated, installed, or tested with the game during this phase.
