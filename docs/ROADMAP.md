# Native port investigation roadmap

Each phase ends with verifiable evidence. Do not jump directly to APK generation.

| Phase | Work | Completion criterion |
| --- | --- | --- |
| 0 — Identification | Record the PC executable's hash, format, and version | Reproducible local executable report |
| 1 — Dependencies | Investigate imports, dynamic loading, platform components, and graphics | List distinguishing observed facts, inferences, and unknowns |
| 2 — Pilot analysis | Select a small pure function, study assembly/pseudocode, and write an original implementation | Documented comparison of inputs and outputs against a reference |
| 3 — Data | Select a simple format and build a reader/viewer | Synthetic fixtures in CI; real game files remain local |
| 4 — Android foundation | Create an ARM64 host for original modules with logging and input | Android build running a validated module; not yet the game |
| 5 — Graphics | Choose a strategy after investigating shaders, passes, and dependencies | Minimal scene reproduced and compared against a reference |
| 6 — Systems | Evaluate animation, physics, scripts, audio, streaming, and saves separately | Functional evidence per system before integration |
| 7 — Integration | Integrate only components whose reconstruction has been validated | Playable scene with behavior and performance tests |

## Next concrete action

Run `tools/inspect_pe.py` on the local copy. Without that executable, no specific address, function, or dependency can be asserted. Then inspect imports with Ghidra/LLVM and choose the first small function to investigate.

## Compatibility execution record, if used as a reference

Record the device, Android version, runtime, CPU translator, Wine version, DXVK version, driver, executable hash, resolution, preset, logs, test scene, and duration. Distinguish CPU crashes, API failures, Vulkan errors, shader problems, input issues, and memory exhaustion. A simple “launches/does not launch” result is insufficient evidence of feasibility.
