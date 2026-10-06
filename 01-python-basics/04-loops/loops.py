#   append()    adds at the end
#   insert()    adds at a specific position
#   remove()    removes by value
#   pop()       removes by index
#   len()       number of elements

grades = [8, 5, 9, 4, 7, 10]

approved_count = 0

for grade in grades:
    if grade >= 7:
        approved_count += 1
        print(grade, "Approved")
    else:
        print(grade, "Failed")


print("Approved count:", approved_count)
