import random as rn
import os
from art import data, logo1, vs

A = rn.choice(data)
B = rn.choice(data)
if A == B:
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
    global A, B
    score_check = 0
    def compare(A, B, follower_check):
        '''Comparing the size of followers on IG'''
        if follower_check == "A" and A['follower_count'] > B['follower_count']:
            return True
        elif follower_check == "B" and B['follower_count'] > A['follower_count']:
            return True
        else:
            return False
    while True:
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
        print(vs)
        print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")
        follower_check = input("Who has more followers? Type 'A' or 'B': ")
        clear()
        print(logo1)
        if compare(A, B, follower_check):
            score_check += 1
            print(f'You are right! Current score: {score_check}')
            switch_values()
        else:
            print(f"Sorry, that's wrong. Final score: {score_check}")
            break


higherlower()
