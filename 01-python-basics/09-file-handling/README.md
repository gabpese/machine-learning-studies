# Lesson 09 – File Handling

[English](README.md) | [Português (BR)](README.pt-BR.md) · [Back to root](../../README.md)

## Focus
Read and write text files safely and build file paths that work on any machine.

## Prerequisites
[Lesson 04](../04-loops), [Lesson 07](../07-error-handling) and [Lesson 08](../08-modules)

## Concepts
- `open(path, "r")` and `open(path, "w")` (`"w"` overwrites the file)
- `with open(...) as file` closes the file automatically
- `.read()` vs iterating line by line
- `.strip()` to remove line breaks and `"\n".join(list)` to build text
- `FileNotFoundError` handling
- `pathlib.Path`: `__file__`, `.resolve()`, `.parents`, the `/` operator
- Path checks and folder creation: `exists()`, `is_file()`, `is_dir()`, `mkdir(parents=True, exist_ok=True)`

## Files
- [file_handling.py](file_handling.py)
- [data.txt](data.txt), [languages.txt](languages.txt), [grades.txt](grades.txt): sample data
- Exercise notes: [exercises](exercises)

## Exercises
1. Build the project paths with `pathlib` instead of hard-coded strings.
2. Write a line to `data.txt` and read the file back.
3. Read `grades.txt`, convert each line to `int` and count the approved grades.
4. Read a list of languages ignoring empty lines, wrapped in `try`/`except FileNotFoundError`.
5. Filter empty values from a list, write the rest to `languages.txt` with `"\n".join()` and read it back.
6. Check whether paths exist and are files or folders, and create result folders.

## Expected outcome
Your script runs from any working directory, reads and writes the sample files, and fails gracefully when a file is missing.

## Why it matters for ML
Datasets, trained models and results all live in files. Reading them reliably is the first step of every ML pipeline.

## Checklist
- [ ] I know why `with` is preferred over manual `close()`
- [ ] I can explain the difference between `"r"` and `"w"`
- [ ] I can build paths with `pathlib` without hard-coding them
