import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def update_resources(coffee_type):
    '''This function updates the resources when each coffee is ordered'''
    global resources
    for ingredient, amount in coffee_type['ingredients'].items():
        if resources[ingredient] < amount:
            print(f"Sorry, we don't have enough {ingredient}.")
            sys.exit()
        resources[ingredient] -= amount
    return resources


def user_choice(coffee, selection):
    '''This function allows the user to pay for the coffee and gives change accordingly'''
    global profit
    print('please insert coins')
    coins = {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickels': 0.05,
        'pennies': 0.01
    }
    total = 0
    for coin, coin_value in coins.items():
        users_coins = input(f'how many {coin}? ')
        total += coin_value * int(users_coins)
    if total >= coffee:
        profit += coffee
        if total == coffee:
            print(f"Thank you for your purchase! Here's your {selection}")
        else:
            change = round(total - coffee, 2)
            print(f"Thank you for your purchase! Your change is ${change:.2f}")
        return True
    else:
        print("Sorry, you don't have enough money to buy this coffee.")
        return False


espresso = MENU["espresso"]
cappuccino = MENU["cappuccino"]
latte = MENU["latte"]
while True:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_choice == 'espresso':
        update_resources(espresso)
        user_choice(espresso['cost'], 'espresso')
    elif coffee_choice == 'cappuccino':
        update_resources(cappuccino)
        user_choice(cappuccino['cost'], 'cappuccino')
    elif coffee_choice == 'latte':
        update_resources(latte)
        user_choice(latte['cost'], 'latte')
    elif coffee_choice == 'report':
        print(f'{resources} and a profit of ${profit}')
    elif coffee_choice == 'off':
        break