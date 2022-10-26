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
    for value in MENU[drink]['ingredients']:
        if value >= resources[value]:
            print(f"Sorry there is not enough {value}.")
            return False
        return True


def change(drink):
    """Returns the amount of change from the transaction"""
    change =  count_money() - MENU[drink][cost]
    return (f"Your change is {change}.")


def count_money():
    """Returns the sum of the coins inserted"""
    print("Please insert coins.")
    total = int(input('How many quarters?')) *.25
    total += int(input('How many dimes?')) *.10
    total += int(input('How many nickels?')) *.05
    total += int(input('How many pennies?')) * .01
    return total 
    
def coffee_machine():
    is_running = True
    while is_running:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'off':
            is_running = False
            print("Turning off the machine")
        
        elif choice == "report":
            print_resources()
            
        check_ingredients(choice)
        count_money()
        change(choice)
        
        print(f"Here is your {choice}☕. Enjoy!")
        is_running = False
        
coffee_machine()    
    
             
    
    # TODO: 2. Check if there is enough resources to make the drink. If not print "Sorry, not enough resources" and continue.
    
    


