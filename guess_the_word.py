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

user_guess = "_" * len(word)

# Convert user_guess to a list
user_guess_list = list(user_guess)

# Convert word to a list
word_list = list(word)


if attempts == 0:
        print(user_guess_list)


while attempts > len(word) and user_guess_list != word_list:
    if user_guess_list == word_list:
        print("\nYou guessed the word correctly!")
        break
    # Ask the user to guess a letter    
    guess = input("Guess a letter: ")
    if guess in word:
        print("\nYes, the word contains the letter:", guess)
        # Find the index of the letter in the word
        for index in range(len(word)):
            if word[index] == guess:
                user_guess_list[index] = guess
        # Print the index of the guessed letter
        print("\nThe index of the letter is:", index)
        # Replace the underscore with the letter
        print(user_guess_list)
        print(word_list)
        

    else:
        print("\nYou have lost a life!. You have", len(word) - attempts, "attempts left.")
        print(user_guess_list)
        attempts += 1

