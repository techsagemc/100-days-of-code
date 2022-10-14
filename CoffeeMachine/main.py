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
Money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. Print report to show current resource


def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f'Money: ${Money}')
      
    
        
def check_ingredients(drink):
    for ingredient, amount in drink['ingredients'].items():
        if resources[ingredient] < amount:
            print("Sorry, not enough ingredients")
            coffee_machine()
       
            

def count_money():
    
    quarters = .25 * num_of_quarters
    dimes = .10 * num_of_dimes
    nickels = .05 * num_of_nickels
    pennies = .01 * num_of_pennies
    
 



def change(cost):
    for item, value in MENU[cost]:
        change = quarters + dimes + nickels + pennies
        
          


def coffee_machine():
    is_running = True
    while is_running:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'off':
            is_running = False
            print("Turning off the machine")
        
        elif choice == "report":
            print_resources()   
            coffee_machine()
        
        print("Please insert coins.")
        num_of_quarters = int(input('How many quarters?'))
        num_of_dimes = int(input('How many dimes?'))
        num_of_nickels = int(input('How many nickels?'))
        num_of_pennies = int(input('How many pennies?'))
        
        count_money()
        check_ingredients()
        change(cost = choice)
        
        print(f"Here is your {choice}☕. Enjoy!")
        is_running = False
        
coffee_machine()    
    
             
    
    # TODO: 2. Check if there is enough resources to make the drink. If not print "Sorry, not enough resources" and continue.
    
    

