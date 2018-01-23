*import string
import random

"""
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick a random item from the list
3. Hide the word (use *)
4. Reveal the letters already guessed
5. Create the win conditions

"""
word_list = ["chickens", "fish", "are", "is", "type", "of", "lettuce", "and", "cows", "cheese"]
won = False
guesstaken = 10
phrase = 10
w1 = (word_list[random.randint(1, 10)])
w2 = (word_list[random.randint(1, 10)])
w3 = (word_list[random.randint(1, 10)])
w4 = (word_list[random.randint(1, 10)])
`w5 = (word_list[random.randint(1, 10)])
w6 = (word_list[random.randint(1, 10)])
w7 = (word_list[random.randint(1, 10)])
w8 = (word_list[random.randint(1, 10)])
w9 = (word_list[random.randint(1, 10)])
w10 = (word_list[random.randint(1, 10)])
letters = string.ascii_letters
print(string.ascii_lowercase(letters))

all_ws = (w1, w2, w3, w4, w5, w6, w7, w8, w9, w10)

while guesstaken > 0 and won is False:
    if guesstaken > 0:
        print(all_ws)
        guesstaken -= 1