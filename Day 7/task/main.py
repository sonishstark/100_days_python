import random
from traceback import print_tb

word_list = ["aardvark", "baboon", "camel"]
lives = 6
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
place_holder = "_" * length
print(place_holder)

game_over = False
correct_letters = []
while not game_over:

    guess = input("Guess a letter from one the word above : ").lower()

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
    #  is, "Wrong" if it's not.

    #lenght = len(chosen_word)
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win")
