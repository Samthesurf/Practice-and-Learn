import random as rn
import os
from art import logo2


def clear():
    '''this clears the terminal'''
    os.system('cls')


def number_game():
    '''This is a number guessing game function'''
    print("Welcome to the number guessing game \nI am thinking of a number between 1 and 100")
    numbers = [x for x in range(1, 101)]
    computers_choice = rn.choice(numbers)

    def guess():
        '''The criteria for guessing the number'''
        your_choice = int(input("What's the number? "))
        if computers_choice == your_choice:
            print(f"Psst, the number is {computers_choice}")
            return True
        elif computers_choice > your_choice:
            print(f"Too low")
        else:
            print(f'Too high')
        return False
        
    def easy():
        '''If difficulty is easy'''
        num_choices = 10
        for i in range(num_choices):
            print(f"You have {num_choices-i} chances left")
            if guess():
                print(f'Psst you guessed correctly, the random number was {computers_choice}')
                return
        print('Game over, you lost')
            
    def hard():
        '''If difficulty is hard'''
        num_choices = 5
        for i in range(num_choices):
            print(f"You have {num_choices-i} chances left")
            if guess():
                print(f'Psst you guessed correctly, the random number was {computers_choice}')
                return
        print('Game over, you lost')

    while True:
        difficulty = input('Choose your difficulty between easy and hard (or type "exit" to quit): ')
        if difficulty == 'easy':
            easy()
        elif difficulty == 'hard':
            hard()
        elif difficulty == 'exit':
            print('Thanks for playing!')
            break
        else:
            print('Invalid input, please try again.')

    while True: 
        if input("Do you want to restart the game? Type 'y' for  yes and 'n' for no: ") == 'y':
            clear()
            number_game()
        else: 
            print('Game over')
            break

number_game()
