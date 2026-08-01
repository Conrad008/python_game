import os
import random

LEADERBOARD_FILE = "high_scores.txt"

def get_hint(secret_number):
    hints = []

    # Divisibility hint
    for divisor in [2, 3, 5, 10]:
        if secret_number % divisor == 0:
            hints.append(f"The number is divisible by {divisor}.")
            break

    # Even/Odd hint
    if not hints:
        if secret_number % 2 == 0:
            hints.append("The number is Even.")
        else:
            hints.append("The number is Odd.")

    # Range hint
    lower_bound = max(1, secret_number - (secret_number % 10))
    upper_bound = min(100, lower_bound + 10)
    hints.append(f"The number is between {lower_bound} and {upper_bound}.")

    return random.choice(hints)

def save_score(username, score):
    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{username},{score}\n")


def display_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        print("\n--- Leaderboard ---")
        print("No high scores yet! Cement yourself as the Best!")
        return

    scores = []
    with open(LEADERBOARD_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                name, attempts = line.split(",")
                scores.append((name, int(attempts)))

    scores.sort(key=lambda x: x[1])

    print("\n --- LEADERBOARD (Top 5) --- ")
    for rank, (name, attempts) in enumerate(scores[:5], start=1):
        print(f"{rank}. {name} - {attempts} attempt(s)")
    print("-------------------------------\n")

def select_difficulty():
    levels = {"1": ("Easy", 10), "2": ("Medium", 7), "3": ("Hard", 5)}

    while True:
        print("\nSelect Difficulty:")
        print("1. Easy (10 attempts)")
        print("2. Medium (7 attempts)")
        print("3. Hard (5 attempts)")

        choice = input("Enter choice (1-3): ").strip()
        if choice in levels:
            name, attempts = levels[choice]
            print(f"\nYou selected {name} mode! You have {attempts} attempts.")
            return attempts
        else:
            print("Invalid selection. Please enter 1, 2, or 3.")

def play_game():
    print(" WELCOME TO THE NUMBER GUESSING GAME! ")
    print("I'm thinking of a number between 1 and 100.")

    username = input("\nEnter your username: ").strip()
    if not username:
        username = "Player"

    max_attempts = select_difficulty()
    secret_number = random.randint(1, 100)
    attempts = 0
    wrong_attempts = 0

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"\nRemaining guesses: {remaining}")

        try:
            guess = int(
                input(
                    f"Attempt {attempts + 1}/{max_attempts} - Guess a number (1-100): "
                )
            )
        except ValueError:
            print(" Please enter a valid integer.")
            continue

        if not 1 <= guess <= 100:
            print(" Out of range! Guess a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret_number:
            print(
                f"\n Congratulations, {username}! You guessed the number {secret_number} in {attempts} attempt(s)!"
            )
            save_score(username, attempts)
            break
        elif guess < secret_number:
            print(" Too Low!")
            wrong_attempts += 1
        else:
            print(" Too High!")
            wrong_attempts += 1

        # Give a hint after 3 wrong attempts
        if wrong_attempts == 3 and attempts < max_attempts:
            print(f"\n HINT: {get_hint(secret_number)}")

    else:
        print(
            f"\n Game Over! You ran out of attempts. The secret number was {secret_number}."
        )

    display_leaderboard()


if __name__ == "__main__":
    while True:
        play_game()
        again = input("Do you want to play again? (yes/n0): ").strip().lower()
        if again != "yes":
            print("Thanks for playing! Goodbye!")
            break    