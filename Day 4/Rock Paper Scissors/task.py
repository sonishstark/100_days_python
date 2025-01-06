rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
number = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))

if number == "2":
    print(scissors)
    print("Computer chose")
    print(scissors)
    print("It's a draw")
elif number == "1":
    print(paper)
    print("Computer chose")
    print(scissors)
    print("You lose")
else:
    print(rock)
    print("Computer Chose")
    print(rock)
    print("It's a draw")
