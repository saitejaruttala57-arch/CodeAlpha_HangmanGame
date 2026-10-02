import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "college"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Create hidden word
display_word = ["_"] * len(word)

while incorrect_guesses < max_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", guessed_letters)
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("✅ Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")

# Game result
if "_" not in display_word:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)