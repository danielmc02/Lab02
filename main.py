"""Three Card Monte
Author: Jimmy Le
Date: 09/05/2025

Simple guessing / wagering game: find the Queen among three cards.
Player starts with $100 and may bet each round. If the player guesses
correctly they receive double their bet (net gain of 2x bet as specified).
Game ends when player chooses to stop or runs out of money.
"""

import random
import check_input
from check_input import get_positive_int, get_yes_no


def get_users_bet(money: int) -> int:
    """Prompt for bet (1..money). Uses check_input for validation.
    Returns the validated bet amount (>0)."""
    print(f"You have ${money}")
    # Reuse provided positive int, then range-check.
    while True:
        bet = get_positive_int(f"Enter bet (1-{money}): ")
        if bet == 0:
            print("Bet must be at least 1.")
        elif bet > money:
            print("Insufficient funds.")
        else:
            return bet


def get_users_choice() -> int:
    """Display face‑down cards and return user's guess (1-3)."""
    print_default_cards()
    # Use check_input range helper to guarantee valid int in range.
    return check_input.get_int_range("Choose a card (1-3): ", 1, 3)


def display_queen_loc(queen_loc: int) -> None:
    """Show cards with queen (1-based index)."""
    layouts = {
        1: [" Q ", " K ", " K "],
        2: [" K ", " Q ", " K "],
        3: [" K ", " K ", " Q "]
    }
    trio = layouts[queen_loc]
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print(f"|{trio[0]}| |{trio[1]}| |{trio[2]}|")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")


def print_default_cards():
    """Show numbered face-down cards."""
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  1  | |  2  | |  3  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")


def main():
    money = 100
    print("- Three Card Monte -\nFind the queen to double your bet!\n")

    while money > 0:
        queen_loc = random.randint(1, 3)  # 1-based for simplicity
        bet = get_users_bet(money)
        guess = get_users_choice()

        # Evaluate before revealing queen visually
        if guess == queen_loc:
            winnings = bet * 2  # Requirement text: receive double their bet
            money += winnings
            print(f"Correct! You win ${winnings}.")
        else:
            money -= bet
            print("Incorrect.")

        display_queen_loc(queen_loc)
        print(f"Balance: ${money}\n")

        if money <= 0:
            print("You're out of money. Game over.")
            break
        if not get_yes_no("Play again (Y/N)? "):
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
