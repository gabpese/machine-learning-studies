grades = [8, 5, 9, 7, 4, 10]


def analyze_grades(grades, minimum_grade=7):
    approved = 0

    for grade in grades:
        if grade >= minimum_grade:
            approved += 1

    return approved


result_1 = analyze_grades(grades)
print("Approved count:", result_1)

result_2 = analyze_grades(grades, minimum_grade=9)
print("Approved count (minimum grade 9):", result_2)
