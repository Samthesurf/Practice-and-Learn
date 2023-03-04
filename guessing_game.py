import random as rn
import os
from art import logo2


def clear():
    '''this clears the terminal'''
    os.system('cls')


def number_game():
    '''This is a number guessing game function'''
    print(logo2)
    print("Welcome to the number guessing game \nI am thinking of a number between 1 and 100")
    numbers = [x for x in range(1, 101)]
    computers_choice = rn.choice(numbers)

    def guess():
        '''The criteria for guessing the number'''
        your_choice = int(input("What's the number? "))
        if computers_choice == your_choice:
            print(f"Psst, the number is {computers_choice}")
            return True  # placeholder for when the guess actually becomes true aka equal to the computer's choice
        elif computers_choice > your_choice:
            print(f"Too low")
            return False  # placeholder for when the guess is false, not necessary
        else:
            print(f'Too high')
            return False  
        
    def easy():
        '''If the difficulty is easy'''
        num_choices = 10
        while num_choices > 0:
            print(f"You have {num_choices} chances left")
            num_choices -= 1
            if guess():  # if the guess function is true (return True), going back to the guess function, means the guessed number is equal to the computer's choice
                print(f'Psst you guessed correctly, the random number was {computers_choice}')
                return
        print('Game over, you lost')
            
    def hard():
        '''If the difficulty is hard'''
        num_choices = 5
        for i in range(num_choices):
            print(f"You have {num_choices-i} chances left")  # it does 5-1,5-2,5-3, etc until it does it 5 times, which equals 0 chances left
            if guess():
                print(f'Psst you guessed correctly, the random number was {computers_choice}')
                return  # ending the loop
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
            number_game() # absolutely just copied this from my blackjack game, because recursion seems cool to me
        else: 
            print('Game over')
            break


number_game()