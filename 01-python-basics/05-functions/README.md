# Lesson 05 – Functions

[English](README.md) | [Português (BR)](README.pt-BR.md) · [Back to root](../../README.md)

## Focus
Package reusable logic into functions with parameters and return values.

## Prerequisites
[Lesson 04](../04-loops)

## Concepts
- `def` and calling a function
- Parameters and default values (`minimum_grade=7`)
- Keyword arguments (`minimum_grade=9`)
- `return` vs `print`
- Reusing the same function with different inputs

## Files
- [functions.py](functions.py)

## Exercises
1. Turn the pass-count loop from Lesson 04 into a function `analyze_grades(grades, minimum_grade=7)`.
2. Call it with the default pass mark and with a custom one.
3. Make the function return the result and print it outside.

## Expected outcome
You can wrap a piece of logic in a function, give it sensible defaults and reuse it without copying code.

## Why it matters for ML
Preprocessing steps, metrics and training routines are all functions. Defaults and keyword arguments are exactly how libraries like scikit-learn are configured.

## Checklist
- [ ] I can explain the difference between a parameter and an argument
- [ ] I know when to use a default value
- [ ] My functions return values instead of only printing
