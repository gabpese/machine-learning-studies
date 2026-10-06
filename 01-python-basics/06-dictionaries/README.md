# Lesson 06 – Dictionaries

[English](README.md) | [Português (BR)](README.pt-BR.md) · [Back to root](../../README.md)

## Focus
Represent structured data with key/value pairs.

## Prerequisites
[Lesson 05](../05-functions)

## Concepts
- Creating dictionaries `{"key": value}`
- Reading with `dict["key"]` and safely with `dict.get("key", default)`
- `.items()`, `.keys()`, `.values()`
- Lists of dictionaries
- `KeyError` when a key does not exist

## Files
- [dictionaries.py](dictionaries.py)

## Exercises
1. Model a course, a person, a user and two products as dictionaries.
2. Write functions that print the items, keys and values of any dictionary.
3. Write `check_product()`, which says whether a product is available using `.get("stock", 0)`.
4. Loop over a list of dictionaries and apply the functions to each.

## Expected outcome
You can represent a real-world record as a dictionary, iterate over it and read missing keys without crashing.

## Why it matters for ML
Records from JSON/APIs, model hyperparameters and result reports are dictionaries. A Pandas row behaves much like one.

## Checklist
- [ ] I can explain the difference between `dict["key"]` and `dict.get("key")`
- [ ] I can iterate over keys, values and items
- [ ] I did the exercises without looking at the code
