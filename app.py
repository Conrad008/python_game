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