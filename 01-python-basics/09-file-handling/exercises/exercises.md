# Lesson 09 – Exercise Notes

## Exercise 1: Checking paths

- "Does this path exist?" -> `exists()`
- "Does this path represent a file?" -> `is_file()`
- "Does this path represent a folder?" -> `is_dir()`

## Exercise 2: Creating a folder

```python
RESULTS_FOLDER.mkdir(exist_ok=True)
```

## Exercise 3: Creating nested folders

```python
PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)
```

## Exercise 4: Checking before reading

```python
if GRADES_PATH.exists()
```

## Challenge

_To be completed._
