# OOP_Coffee_Maker
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def machine_start():
    my_menu=Menu()
    take_money=MoneyMachine()
    coffee=CoffeeMaker()
    
    is_on=True
    print("**********Let's Fresh your Day With Coffee************")
    while is_on:
        # let's discuus menu first
        # prompting a user that what would they like
        # my_menu=Menu()
        select=str(input("What would you like? (espresso/latte/cappuccino/report/off):")).lower()

        if select =="off":
            is_on=False
            print("machine shutting down..")
        elif select=="report":
            print(coffee.report())
            take_money.report() 
        else:
            selected=my_menu.find_drink(order_name=select)
            print(selected.ingredients)  
            # so now from that order name i have to check ingrideint of that coffee
            # from this CoffeeMaker we will see that is that sufficient ingrident are there or not
            if coffee.is_resource_sufficient(selected) and take_money.make_payment(cost=selected.cost):
              
            # take_money=MoneyMachine()
            # take_money.process_coins()
            # coffee_cost=selected.cost #this line will assign cost of our selected coffee
              #this line of code will check the cost and take the money from user
                coffee.make_coffee(order=selected) #after making payment this object make coffee for our user
            
machine_start()