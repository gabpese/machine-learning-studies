# Machine Learning Studies

[English](README.md) | [Português (BR)](README.pt-BR.md)

> From Python basics to Machine Learning, one lesson at a time.

## About

This repository documents my learning path from **zero Python** to **Machine Learning**.

Every line of code here was typed by me, by hand, with no AI-generated code. The goal is to learn, not to ship fast. An AI assistant is used only as a *teacher*: it plans lessons, explains concepts and reviews my understanding.

Each lesson is documented with its **focus**, **exercises** and **expected outcome**, so the repository can also be followed by anyone who wants to take the same path.

## How to use this repository

1. Follow the phases and lessons **in order**.
2. Read the lesson's `README.md` before touching the code.
3. Try the exercises **without** looking at the code first.
4. Compare your result with the lesson's *expected outcome*.
5. Use the checklist at the end of each lesson to verify that you can explain the topic with your own words.

## Roadmap

| Phase | Folder | Topic | Status |
|-------|--------|-------|--------|
| 01 | `01-python-basics` | Python fundamentals | 🚧 In progress |
| 02 | `02-python-for-data` | NumPy, Pandas, data visualization | ⏳ Planned |
| 03 | `03-math-stats` | Math and statistics for ML | ⏳ Planned |
| 04 | `04-ml-fundamentals` | Regression, classification, evaluation | ⏳ Planned |
| 05 | `05-classical-ml` | Trees, ensembles, clustering, pipelines | ⏳ Planned |
| 06 | `06-deep-learning-intro` | Neural networks | ⏳ Planned |

## Phase 01 – Python Basics

| # | Lesson | Focus | Status |
|---|--------|-------|--------|
| 01 | [First Program](01-python-basics/01-first-program) | `print`, basic types, `type()`, casting | ✅ |
| 02 | [Variables](01-python-basics/02-variables) | Variables and arithmetic | ✅ |
| 03 | [Conditionals](01-python-basics/03-conditionals) | `if`/`elif`/`else`, `and`/`or`/`not` | ✅ |
| 04 | [Loops](01-python-basics/04-loops) | `for`, lists, counters | ✅ |
| 05 | [Functions](01-python-basics/05-functions) | `def`, parameters, default values, `return` | ✅ |
| 06 | [Dictionaries](01-python-basics/06-dictionaries) | key/value data, `.items()`, `.get()` | ✅ |
| 07 | [Error Handling](01-python-basics/07-error-handling) | `try`/`except`/`else`/`finally` | ✅ |
| 08 | [Modules and Packages](01-python-basics/08-modules) | `import`, own modules, packages | ✅ |
| 09 | [File Handling](01-python-basics/09-file-handling) | `open`, `with`, `pathlib` | ✅ |
| 10 | Lists, Tuples and Sets | comprehensions | ⏳ |
| 11 | Object-Oriented Programming | classes, inheritance | ⏳ |
| 12 | Virtual Environments and pip | `venv`, `requirements.txt` | ⏳ |
| 13 | JSON and CSV | standard library | ⏳ |
| 14 | **Project 1** | CLI app using everything above | ⏳ |


## Lesson README template

Every lesson folder contains a `README.md` (English) and a `README.pt-BR.md` (Portuguese) with:

- **Focus**: what the lesson teaches
- **Prerequisites**: lessons to have done before
- **Concepts**: the key ideas
- **Exercises**: what to practice
- **Expected outcome**: what you should be able to do afterwards
- **Why it matters for ML**: how it connects to the goal
- **Checklist**: self-assessment

## Setup

```bash
# clone
git clone https://github.com/<your-user>/machine-learning-studies.git
cd machine-learning-studies

# create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux / macOS

# install dependencies (empty until Phase 02)
pip install -r requirements.txt
```

Run any lesson from inside its own folder, for example:

```bash
cd 01-python-basics/08-modules
python modules.py
```

## Conventions

- Folder and file names are in **English**.
- Code identifiers, comments and output messages are in **English**.
- Commits follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `chore:`, `docs:`).

## Author

**Gabriel Pesegoginski**
