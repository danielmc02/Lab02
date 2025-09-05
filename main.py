""" LAB #2
    09/05/2025
    Student 1: Daniel McCray
    Student 2: Jimmy Le

    Three Card Monte: find the Queen among three cards.
    Player starts with $100 and may bet each round. If the player guesses
    correctly they receive double their bet. Game ends when player chooses
    to stop or runs out of money.
"""

import random
from check_input import get_yes_no, get_positive_int, get_int_range


def get_users_bet(money):
    # Ask player for bet; has to be in range and cannot be 0.
    print(f"You have ${money}")
    while True:
        bet = get_positive_int(f"Enter bet (1-{money}): ")
        if bet == 0:
            print("Bet must be at least 1.")
        elif bet > money:
            print("Insufficient funds.")
        else:
            return bet


def get_users_choice():
    # Show face-down cards and return user's guess 1-3.
    print_default_cards()
    return get_int_range("Choose a card (1-3): ", 1, 3)


def display_queen_loc(queen_loc):
    # Reveal queen position
    symbols = ["K", "K", "K"]
    symbols[queen_loc - 1] = "Q"  # put queen in chosen slot
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print(f"|{symbols[0]:^5}| |{symbols[1]:^5}| |{symbols[2]:^5}|")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")


def print_default_cards():
    # Show the 3 face-down card spots (just numbers).
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  1  | |  2  | |  3  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")


def main():
    money = 100  # starting bankroll
    print("Three Card Monte - try to find the Queen to win your bet!\n")

    while money > 0:
        queen_loc = random.randint(1, 3)  # new random spot each round
        bet = get_users_bet(money)
        guess = get_users_choice()

        if guess == queen_loc:
            # Per assignment: player "gains the amount of the bet" when correct
            money += bet
            print(f"Nice! You found the queen. You win ${bet}.")
        else:
            money -= bet
            print("Incorrect.")

        display_queen_loc(queen_loc)
        print(f"Balance: ${money}\n")

        if money <= 0:
            print("You lose, beat it loser.")
            break
        if not get_yes_no("Play again (Y/N)? "):
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()