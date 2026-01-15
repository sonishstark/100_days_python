bmi = 84 / 1.65 ** 2
print(bmi)

#removes the decimal
print(int(bmi))

#if the first decimal number is greater than 5 prints up or else down (Ex: 31.788 = 32, 31.433 = 31)
print(round(bmi))

#two decimal places
print(round(bmi,2))

score = 0

score += 1
print(score)

print("you score is " + str(score))

score1 = 2
height =1.8
is_winning = True
#fstring
print(f"Your score is = {score} and your height is {height} so winning is {is_winning}")
