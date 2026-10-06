# Lesson 03 – Conditionals

[English](README.md) | [Português (BR)](README.pt-BR.md) · [Back to root](../../README.md)

## Focus
Make the program take different paths depending on conditions.

## Prerequisites
[Lesson 02](../02-variables)

## Concepts
- `if`, `elif`, `else`
- Comparison operators: `>=`, `==`, `!=`, ...
- Logical operators: `and`, `or`, `not`
- Boolean variables used directly as conditions
- Order of the checks matters (most specific first)

## Files
- [conditionals.py](conditionals.py)

## Exercises
1. Write an entry validation: VIP, regular ticket or denied, based on age, ticket, blocked status and VIP status.
2. Change the variables to exercise every branch.
3. Add a final message that prints regardless of the branch taken.

## Expected outcome
You can build a rule-based decision with several conditions and trace by hand which branch will run.

## Why it matters for ML
Decision rules are the intuition behind decision trees. Data cleaning also relies on conditions (e.g. discard invalid rows).

## Checklist
- [ ] I can explain `and`, `or` and `not`
- [ ] I know why `elif` order matters
- [ ] I tested every branch
