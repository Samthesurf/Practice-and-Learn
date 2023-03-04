import random as rn
import os
from art import data, logo1, vs

A = rn.choice(data)
B = rn.choice(data)


def clear():
    '''this clears the terminal'''
    os.system('cls')
#  do the printing


def switch_values():
    ''' use a temporary variable to hold the value of B'''
    global A, B
    A, B = B, rn.choice(data)
    return B


def higherlower():
    '''The function for the higher lower game'''
    print(logo1)
    global A
    global B
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")

    def compare(A, B):
        '''Comparing the size of followers on IG'''
        score_check = 0
        while True:
            score_check += 1
            follower_check = input("Who has more followers? Type 'A' or 'B': ")
            if follower_check == "A" and A['follower_count'] > B['follower_count']:
                clear()
                print(f'You are right! Current score: {score_check}')
                switch_values()
                higherlower()
                return True
            elif follower_check == "B" and B['follower_count'] > A['follower_count']:
                clear()
                print(f'You are right! Current score: {score_check}')
                switch_values()
                higherlower()
                return True
            else: 
                clear()
                print(f"Sorry, that's wrong. Final score: {score_check}")
                return False
    
    compare(A, B)


higherlower()
