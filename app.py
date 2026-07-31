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