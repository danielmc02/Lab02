from check_input import get_positive_int, get_yes_no
import random






def main():

    # ! INIT VARIABLES 
    global starting_money 
    global randomized_queen_location 
    global users_guess
    users_guess = ""

    starting_money = 100
    card_list = [False,False,False]



    print("-Three card Monte-\nFind the queen to double your bet!\n\n")



    while True:
        randomized_queen_location = random.randrange(0,3)

        for index in range(3):
            if(index == randomized_queen_location):
                card_list[index] = True

            else:
                card_list[index] = False
        #? get bet
        user_bet = get_users_bet(starting_money)
     
        
        #! Subtract 1 from users guess to match list index offset.
        #? In reality a human guess is list index + 1 because we count from 0

        users_guess = get_users_choice()

        users_guess_int = int(users_guess) -1

        display_queen_loc(randomized_queen_location)
        #print(f"users guess is {str(users_guess_int)}, queen loc is {randomized_queen_location} ")
        if(users_guess_int == randomized_queen_location):
            print("Congratulations, you got lucky")
            print(f"You won {user_bet*2}")
            # add currency to account
            starting_money += (user_bet*2)
            print(f"Total balance is now: {starting_money}")
        else:
            print("Sorry but your bet is incorrect")
            starting_money = starting_money-user_bet
            print(f"Total balance is now: {starting_money}")
     
        if(starting_money <= 0):
            print("You lose, beat it loser")
            break

        elif get_yes_no("Would you like to play again "):
            #loop again
            print()
        else: 
            # if they enter no or n, break the program
            break







    # ? Display the cards with proper index
    # ? Becasue its always 1-3 just manually print 1-3 cards
    
def get_users_choice():
    print_default_cards()
        
    while True:
        users_guess = input("Find the queen: ")
        if int(users_guess) >= 1 and int(users_guess) <=3:
                # Valid value
            break
        else:
            print("Invalid range: Please guess 1-3")

    return users_guess
            

   
def print_default_cards():
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  1  | |  2  | |  3  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")

def display_queen_loc(queen_index):
    # Because there are only 3 variations, we use hardcoded print values. This wouldn't be sustainable @ scale
    if(queen_index == 0):
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  Q  | |  K  | |  K  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")
    elif(queen_index == 1):
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  K  | |  Q  | |  K  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")
    elif(queen_index == 2):
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  K  | |  K  | |  Q  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")


def get_users_money():
    return starting_money



def get_users_bet(money):
    #? Basesd on the example, assume that we inform them their current balance before they bet... makes sense tbh
    print(f"You have ${money}")
    while True:
     users_bet = get_positive_int(f"How much would you like to bet? (Enter between 1-{money}) ")
     if(users_bet > money):
           print(f"Unavailible funds, you only have {money}")
     elif (users_bet <= money and users_bet >= 1):   
        break
     
    return users_bet

if __name__ == "__main__":
    main()

