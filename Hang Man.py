import string
import random

"""
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick a random item from the list
3. Hide the word (use *)
4. Reveal the letters already guessed
5. Create the win conditions
"""

word_list = ["abcdefghijklmnopqrstuvwxyz", "fish", "are", "is", "type", "of", "lettuce", "and", "cows", "waifu"]
ran_word = random.choice(word_list)
A_Z = list(string.ascii_uppercase)
guess_taken = 10
won = False
guessed_letters = []
guess_on = 0

while guess_taken > 0 and won is False:
    output = []
    for letter in ran_word:
        if letter in guessed_letters:
            output.append(letter)
        else:
            output.append("*")
    print(output)
    guess_taken -= 1
    guess = input("Guess a letter")
    guess_lowered = guess.lower()
    guessed_letters.append(guess_lowered)
    if guess_lowered in A_Z:
        A_Z.remove(guess_lowered)
        guess_taken += 1
    elif guessed_letters in A_Z:
        guess_taken -= 1
    elif guess_taken == 0:
        won = True
        print("You are out of guesses you have lost")