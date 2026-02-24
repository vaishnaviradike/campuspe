
import random

print("======================================")
print("      ROCK PAPER SCISSORS")
print("          BEST OF 5 ")
print("======================================")

options = ["rock", "paper", "scissors"]

while True:
    user_score = 0
    computer_score = 0
    round_number = 1

    while user_score < 3 and computer_score < 3:
        print(f"\n--------- Round {round_number} ---------")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Enter your choice (1-3): ")

        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Try again.")
            continue

        user_choice = options[int(choice) - 1]
        computer_choice = random.choice(options)

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie! ")

        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win this round! ")
            user_score += 1

        else:
            print("Computer wins this round! ")
            computer_score += 1

        print("Score → You:", user_score, "| Computer:", computer_score)
        round_number += 1

    print("\n======================================")
    print("           FINAL RESULT")
    print("======================================")

    if user_score == 3:
        print(" CONGRATULATIONS! YOU WON BEST OF 5!")
    else:
        print(" COMPUTER WON BEST OF 5!")

    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Thanks for playing! ")
        break