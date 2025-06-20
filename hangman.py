import random

# Step 1: Predefined words list
words = ["python", "hangman", "developer", "program", "code"]
word_to_guess = random.choice(words)

# Step 2: Setup
guessed_letters = []
attempts = 6
display_word = ["_"] * len(word_to_guess)

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.")

# Step 3: Main game loop
while attempts > 0 and "_" in display_word:
    print("\nWord to guess: " + " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

# Step 4: Game result
if "_" not in display_word:
    print(f"\n🎉 Congratulations! You guessed the word: {word_to_guess}")
else:
    print(f"\n💀 Game Over! The word was: {word_to_guess}")
