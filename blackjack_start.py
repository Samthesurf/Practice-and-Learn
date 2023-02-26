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

    def deal_cards(card):
        random_deal = rn.randrange(len(cards)-1)  # random number between 0 and 12
        card.append(cards[random_deal])  # adds a random card to the list

    def calculate(args):
        '''This function calculates the sum of cards and accounts for an Ace'''
        summed_cards = sum(args)
        if summed_cards == 21:
            return blackjack
        new_args = []
        for n in args:
            if summed_cards > 21 and n == 11:
                new_args.append(1)
            else:
                new_args.append(n)
        return sum(new_args)
    user_card = []
    computer = []
    condition = True
    for _ in range(2):
        deal_cards(user_card)
        deal_cards(computer)
    calculate(user_card)
    calculate(computer)
        
    print(f"This is your card {user_card}")
    print(f"This is one of the computer's cards {rn.choice(computer)}") 

    def compare():
        '''This function checks if the user has lost, won or drew with the computer'''
        user_score = calculate(user_card)
        computer_score = calculate(computer)
        if user_score == computer_score:
            print("It's a draw")
        elif computer_score == blackjack:
            print('You have lost')
        elif user_score == blackjack:
            print('You have won')
        elif user_score > 21:
            print('You have lost')
        elif computer_score > 21:
            print('You have won') 
        else:
            if user_score > computer_score:
                print('You have won')
            elif user_score < computer_score:
                print('You have lost')
        
    while condition:
        answer = input("Do you want to draw another card? Type 'yes' or 'no' ")
        if answer.lower() == 'yes':
            deal_cards(user_card)
            print(f"This is your new card {user_card[-1]}, This is the sum: {calculate(user_card)}")
            print(f"This is the computer's card: {calculate(computer)}")
            if calculate(user_card) and calculate(computer) < 17:
                deal_cards(user_card)
                deal_cards(computer)
                print(f"This is your new card {user_card[-1]}, This is the sum: {calculate(user_card)}")
                print(f"This is the computer's card {computer} and the sum: {calculate(computer)}")
                compare()
            else:
                print(f"This is the computer's card {computer} and the sum: {calculate(computer)}")
                compare()
            return
        else:
            deal_cards(computer)
            compare()
            break

    while condition: 
        if input("Do you want to restart the game? Type 'y' for  yes and 'n' for no: ") == 'y':
            clear()
            blackjackgame()
        else: 
            print('Game over')
            condition = False


blackjackgame()
# phew finally done

