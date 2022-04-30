# Generate a random word and ask the user to guess it.

# import random library
import random

# Create a tuple of words
words = (
    "apple",
    "banana",
    "orange",
    "coconut",
    "strawberry",
    "lime",
    "grapefruit",
    "lemon",
    "kumquat",
    "blueberry",
    "melon",
)

# Random word that will be guessed
word = random.choice(words)

# Comment out later
print("\nThis is the random word:", word +  ".\n")

# Number of attempts the user has to guess the word starts with zero
attempts = 0

# Print the length of the word
print("The word is of length:", len(word), "and you have", len(word), "attempts to guess it.")

while attempts < len(word):
    # Ask the user to guess a letter    
    guess = input("Guess a letter: ")
    if guess in word:
        print("\nYes, the word contains the letter:", guess)
    else:
        print("\nSorry, the word does not contain the letter:", guess)
        attempts += 1

