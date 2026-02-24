stages = [
"""
   ------
   |    |
        |
        |
        |
        |
---------
""",
"""
   ------
   |    |
   O    |
        |
        |
        |
---------
""",
"""
   ------
   |    |
   O    |
   |    |
        |
        |
---------
""",
"""
   ------
   |    |
   O    |
  /|    |
        |
        |
---------
""",
"""
   ------
   |    |
   O    |
  /|\   |
        |
        |
---------
""",
"""
   ------
   |    |
   O    |
  /|\   |
  /     |
        |
---------
""",
"""
   ------
   |    |
   O    |
  /|\   |
  / \   |
        |
---------
"""
]

print("===================================")
print("         HANGMAN GAME :p")
print("===================================")

word = input("Enter the secret word (Player 1): ").lower()


word_length = len(word)
print("The word has", word_length, "letters.")

display = []
for _ in range(word_length):
    display.append("_")

guessed_letters = []
wrong_attempts = 0
max_attempts = len(stages) - 1

while wrong_attempts < max_attempts:

    print(stages[wrong_attempts])
    print("Word:", " ".join(display))

    if "_" not in display:
        print(" YOU WON!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠ Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!:(")
        for i in range(word_length):
            if word[i] == guess:
                display[i] = guess
    else:
        print(" Wrong guess!:o :) ")
        wrong_attempts += 1
        print("Attempts left:", max_attempts - wrong_attempts)

if wrong_attempts == max_attempts:
    print(stages[wrong_attempts])
    print(" GAME OVER!")
    print("The word was:", word)