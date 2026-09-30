# Repository and Termux usage

Public repository: https://github.com/LukeValen/Sekiro-Android-research

## Get the tools

```sh
pkg install python git
git clone https://github.com/LukeValen/Sekiro-Android-research.git
cd Sekiro-Android-research
python -m unittest discover -s tests -v
```

If you already cloned the repository, update it with `git pull --ff-only` instead.

See the README to inspect your local executable. Adjust the path to the file's actual location.

## Contributing

Publish original tools and documentation. Keep game files, executables, DLLs, saves, dumps, and decompilation output local. Review `git status` and `git diff --cached` before each commit. The `.gitignore` helps, but does not provide a complete content check.

A license for the original tools has not been selected yet.
