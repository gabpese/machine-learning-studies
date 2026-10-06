# Lesson 08 – Modules and Packages

[English](README.md) | [Português (BR)](README.pt-BR.md) · [Back to root](../../README.md)

## Focus
Split code into several files and folders, and reuse it with `import`.

## Prerequisites
[Lesson 05](../05-functions) and [Lesson 07](../07-error-handling)

## Concepts
- A module is a `.py` file
- `import module` vs `from module import name`
- Aliases with `as`
- Packages: a folder with `__init__.py`
- `if __name__ == "__main__":` so a file can be both imported and run

## Files
- [modules.py](modules.py): entry point that uses everything below
- [calculator.py](calculator.py): `add`, `subtract`, `multiply`, `divide`
- [conversions.py](conversions.py): safe conversions to `int` and `float`
- [tools/](tools): package with [texts.py](tools/texts.py) (upper/lower case)

## Exercises
1. Create `calculator.py` with four operations and a `main()` guarded by `__main__`.
2. Create `conversions.py` returning `None` on invalid input.
3. Create the `tools` package with `__init__.py` and `texts.py`.
4. In `modules.py`, import with all three styles (`import`, `from ... import`, `as`).
5. Run each file alone and then run `modules.py`.

## Expected outcome
Running `python modules.py` from this folder prints the calculator, conversions and text results, and each module also runs standalone.

## Why it matters for ML
ML projects are organized as packages (data loading, preprocessing, models, evaluation), and every library you will use is imported this way.

## Checklist
- [ ] I can explain what `__name__ == "__main__"` does
- [ ] I know when a folder becomes a package
- [ ] I can choose between the three import styles
