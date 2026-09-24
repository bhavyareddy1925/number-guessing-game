
import random


def show_title():
    print("=" * 50)
    print("          🎯 NUMBER GUESSING GAME")
    print("=" * 50)
    print("Guess the secret number and win points!")
    print()


def choose_difficulty():
    print("Choose Difficulty Level")
    print("1. Easy   (1 - 50, 10 attempts)")
    print("2. Medium (1 - 100, 7 attempts)")
    print("3. Hard   (1 - 200, 5 attempts)")
    print()

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 200, 5
        else:
            print("❌ Invalid choice. Please try again.")


def get_guess(max_number):
    while True:
        try:
            guess = int(input(f"Enter your guess (1-{max_number}): "))

            if 1 <= guess <= max_number:
                return guess
            else:
                print(f"⚠️ Enter a number between 1 and {max_number}.")

        except ValueError:
            print("⚠️ Please enter numbers only.")


def calculate_score(attempts_left):
    return attempts_left * 10


def play_game():
    max_number, max_attempts = choose_difficulty()

    secret_number = random.randint(1, max_number)
    attempts_left = max_attempts

    print("\n🎮 Game Started!")
    print(f"I have selected a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts.")
    print()

    while attempts_left > 0:
        print(f"❤️ Attempts remaining: {attempts_left}")

        guess = get_guess(max_number)

        if guess == secret_number:
            score = calculate_score(attempts_left)

            print("\n🎉 CONGRATULATIONS!")
            print(f"🎯 You guessed the number: {secret_number}")
            print(f"🏆 Your score: {score}")
            return

        elif guess < secret_number:
            print("📈 Too low! Try a higher number.")

        else:
            print("📉 Too high! Try a lower number.")

        attempts_left -= 1
        print()

    print("\n😢 GAME OVER!")
    print(f"The secret number was: {secret_number}")
    print("Better luck next time!")


def main():
    show_title()

    while True:
        play_game()

        print("\n" + "=" * 50)
        again = input("Do you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("\n👋 Thanks for playing!")
            print("Have a great day! 🎯")
            break

        print("\nStarting a new game...\n")


main()