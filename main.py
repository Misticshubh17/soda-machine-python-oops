# all imports
import drinks
import menu
import money_process
import drink_maker

# initialize all objects from imported classes
all_items = drinks.drinks
resources = drinks.resources
money = money_process.MoneyMachine()
menu = menu.Menu(data=all_items)
soda = drink_maker.DrinkMaker(resources=resources)

# get all available drink names from menu
drink_name_str = menu.get_items()

# convert the string of names to a lowercase list
drink_name_list = [i.lower() for i in drink_name_str.split('/')]

# Keep the machine running until user types 'off'
is_machine_on = True
while is_machine_on:
    # Ask user for drink choice
    choice = input(f"What would you like? ({drink_name_str}): ").lower()
    if choice in drink_name_list:     # Check if user's input matches any available drink
        drink = menu.find_drink(choice)
        payment_done = money.transaction(cost=drink['Cost'])
        check_stock = soda.is_resource_sufficient(item=drink)
        if payment_done and check_stock:
            soda.make_drink(order=drink)
    elif choice == 'report':
        soda.report()
    elif choice == 'profit':
        money.report()
    elif choice == 'off':
        print("Machine off. Good Bye!!!")
        is_machine_on = False
    else:
        print(f"We don't sell {choice}.")
