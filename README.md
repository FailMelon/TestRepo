# Git Client Test Repository

A small, dependency-free repository for exercising common Git client workflows.
It contains a Python module and unit test, documentation, CSV data, and a
filename with spaces.

## Try it out

```sh
python -m unittest discover -s tests
git status
```

Useful client checks:

- Edit and stage a tracked file, then unstage it.
- Create and remove an untracked file.
- Rename or delete a tracked file.
- Create a file under `build/` or with a `.log` extension and confirm it is
  ignored.
- Open `notes/ideas & questions.txt` to check paths containing spaces.

No setup or third-party dependencies are required.
