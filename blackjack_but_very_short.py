import random as rn
import os
from art import logo

def clear():
    '''this clears the terminal'''
    os.system('cls')

def blackjackgame():
    '''This function is a simplified game of blackgack'''
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    blackjack = 21
    user_card = []
    computer = []
    deal_cards = lambda card: card.append(rn.choice(cards))
    calculate = lambda args: sum(args) if sum(args) == blackjack else sum([1 if n == 11 and sum(args) > 21 else n for n in args])
    compare = lambda user_score, computer_score: print("It's a draw" if user_score == computer_score else 'You have lost' if computer_score == blackjack or user_score > 21 or computer_score > user_score else 'You have won')
    
    deal_cards(user_card), deal_cards(user_card), deal_cards(computer), deal_cards(computer), calculate(user_card), calculate(computer)
    print(f"This is your card {user_card}\nThis is one of the computer's cards {rn.choice(computer)}")
    
    while True:
        answer = input("Do you want to draw another card? Type 'yes' or 'no' ")
        if answer.lower() == 'yes':
            deal_cards(user_card)
            print(f"This is your new card {user_card[-1]}, This is the sum: {calculate(user_card)}\nThis is the computer's card: {calculate(computer)}")
            compare(calculate(user_card), calculate(computer))
        else:
            while calculate(computer) < 17:
                deal_cards(computer)
            compare(calculate(user_card), calculate(computer))
            break

    if input("Do you want to restart the game? Type 'y' for yes and 'n' for no") == 'y':
        clear()
        blackjackgame()
    else: 
        print('Game over')

blackjackgame()
''' Come back to this function later to see if you fully understand lambda and how it works'''
