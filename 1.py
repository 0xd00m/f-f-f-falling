# Generate a random word and ask the user to guess it.

# import random library

import random

# Create a list of words
words = ['apple', 'banana', 'orange', 'coconut', 'strawberry', 'lime', 'grapefruit', 'lemon', 'kumquat', 'blueberry', 'melon']

word = random.choice(words)

print("This is the random word: ", word, ". Type of the word is: ", type(word))

# find length of the word

length = len(word)

# Print the length of the word

print("The length of the word is: ", length)