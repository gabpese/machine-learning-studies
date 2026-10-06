# Lesson 07 – Error Handling

[English](README.md) | [Português (BR)](README.pt-BR.md) · [Back to root](../../README.md)

## Focus
Anticipate and handle runtime errors so the program does not crash.

## Prerequisites
[Lesson 06](../06-dictionaries)

## Concepts
- Common errors: `TypeError`, `NameError`, `IndexError`, `KeyError`, `ValueError`, `ZeroDivisionError`
- `try` / `except` / `else` / `finally`
- Catching specific exceptions and using `as error`
- Returning `None` to signal failure and checking `is not None`

## Files
- [error_handling.py](error_handling.py)

## Exercises
1. Write `convert_to_integer()` that handles `ValueError` and `TypeError`.
2. Write safe lookups for lists (`IndexError`) and dictionaries (`KeyError`).
3. Write `divide()` handling division by zero and invalid types.
4. Write `validate_number()` using all four blocks and observe the order they run in.

## Expected outcome
You can trigger each error on purpose, explain why it happened and handle it gracefully.

## Why it matters for ML
Real data is dirty: missing values, wrong types and malformed rows. Robust code survives long data pipelines and long training runs.

## Checklist
- [ ] I can name the six errors and what causes each
- [ ] I know when `else` and `finally` run
- [ ] I catch specific errors, not everything
