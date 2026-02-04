'''programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"
}

print(programming_dictionary["Bug"])

programming_dictionary["List"] = "Can store a number of elements"
print(programming_dictionary)

empty_dictionary = {}

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
'''

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for key in student_scores:
    if student_scores[key] >= 91 and  student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and  student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71 and  student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

for grades in student_grades:
    print(student_grades[grades])

