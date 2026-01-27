student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#inbuilt function to add
toal_exam_score = sum(student_scores)
sum = 0

#standard way adding using loops
for score in student_scores:
    sum += score

print(sum)
 #to find the largest
large = 0
for score in student_scores:
    if score > large:
        large = score
print(large)

#to find the smallest
small = student_scores[0]
for score in student_scores:
    if score < small:
        small = score
print(small)
