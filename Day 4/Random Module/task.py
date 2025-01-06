import random
"""#importing another file
import my_module

#prints a random number between the given range
random_integer = random.randint(1, 10)
print(random_integer)
#import and using another file my importing
print(my_module.my_favourite_number)

#prints random number by default between 0 - 1
random_number_2 = random.random() * 10 #now range changes 0 - 10 when multiplied
print(random_number_2)

#prints number between 1 - 10 includes 1 and 10
random_number_3 = random.uniform(1, 10)
print(random_number_3)
"""

random_coin = random.uniform(0, 1)
heads_tails = round(random_coin)
if heads_tails == 0:
    print("Tails")
else:
    print("Head")

