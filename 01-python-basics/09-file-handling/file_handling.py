from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parents[2]
LESSON_FOLDER = PROJECT_ROOT / "01-python-basics" / "09-file-handling"
DATA_PATH = LESSON_FOLDER / "data.txt"
LANGUAGES_PATH = LESSON_FOLDER / "languages.txt"
GRADES_PATH = LESSON_FOLDER / "grades.txt"

print("Current file:", CURRENT_FILE)
print("Project root:", PROJECT_ROOT)
print("Data path:", DATA_PATH)

# with open(DATA_PATH, "w") as file:
#     content = file.write("Ruby")


# languages = []

# with open(DATA_PATH, "r") as file:
#     for line in file:
#         language = line.strip()

#         if language != "":
#             languages.append(language)

# print(languages)

# grades = []
# approved_count = 0

# # next I need to read the grades.txt file
# with open(GRADES_PATH, "r") as file:
#     for line in file:
#         grades.append(int(line.strip()))

# for grade in grades:
#     if grade >= 7:
#         approved_count += 1


# print(approved_count)


# def load_languages():
#     languages = []
#     try:
#         with open(LANGUAGES_PATH, "r") as file:
#             for line in file:
#                 language = line.strip()

#                 if language != "":
#                     languages.append(language)

#         return languages

#     except FileNotFoundError as error:
#         print("File not found", error)
#         return None
#     finally:
#         print("Program finished")

# result = load_languages()

# if result is not None:
#     print(result)


languages = [
    "Python",
    "",
    "Ruby",
    "",
    "JavaScript"
]

valid_languages = []

# Filter out the empty values
for language in languages:
    if language != "":
        valid_languages.append(language)


# Write to the file
with open(LANGUAGES_PATH, "w") as file:
    content = "\n".join(valid_languages)
    file.write(content)
# This line: content = "\n".join(valid_languages)
# takes: ["Python", "Ruby", "JavaScript"]
# and produces a single str: "Python\nRuby\nJavaScript"
# Note that the \n goes between the elements: Python + \n + Ruby + \n + JavaScript
# and not: Python + \n + Ruby + \n + JavaScript + \n


# Read the file
with open(LANGUAGES_PATH, "r") as file:
    content = file.read()


print(content)
