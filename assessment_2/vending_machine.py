"""
---------------------------------
[ Assessment 2 - Ethan Grajo ]
[ Vending Machine ]
---------------------------------
Started - November 19, 2024
Finished - November 20, 2024

@@ IMPORTANT NOTE TO ANY EDUCATORS/TUTORS VIEWING @@
The script will only work as intended together with the item_stock.db file.
If you decide to test on a local machine, ensure that the database file is
installed along with this file in the same folder.

"""

import sqlite3
import datetime

db = sqlite3.connect('item_stock.db')
admin_password = "12345"

# --------------------------- #
# main functions
# --------------------------- #
def main():
    print(f"{'-'*20} Vending Machine {'-'*20}")
    while True:
        try:
            view_choice = int(input("Would you like to:\n[1] View all items\n[2] View items by category\n>: ")) # gives users the options to either sort the available items or display all items
            if view_choice == 1 or view_choice == 2: # an error exception which is used in different places through this program. 
                break
            else:
                print('Invalid choice. Try again.')
        except ValueError:
            print('Invalid choice. Try again.')

    if view_choice == 1:
        display_all()
    elif view_choice == 2:
        display_specific()

def administrator_check(): # this is a function/feature within the vending machine that lets you restock items in the vending machine as well as see the transaction log
    while True:
        try:
            choice = int(input("Welcome to the vending machine.\nAre you an administrator?\n[1] Yes\n[2] No\n>: "))
            if choice == 1 or choice == 2:
                break
            else:
                print("Invalid selection. Please try again")
        except ValueError:
            print("Invalid selection. Please try again")

    if choice == 1: # agree: administrator check
        attempts = 5 # the amount of attempts a user has before being booted out of the administrator view
        while True:
            pw_check = input("Please enter the administrator password:\n>: ")
            if pw_check == admin_password: # validate password
                break
            else: # will run if password is wrong, attempts will be decreased and when attempts are used up, will boot out of admin view
                attempts -= 1
                if attempts > 0:
                    print(f"Wrong password. {attempts} attempts remaining.")
                else:
                    print("Ran out of attempts. Exiting administrator view.")
                    return # ends the function, forcing the user into the main view
        administrator_view() # runs the admin panel on successful password entry
        return # stops the check on successful entry
    elif choice == 2: # disagree: return to menu
        return

def administrator_view():
        while True:
            try:
                choice = int(input("Welcome to administrator mode.\nWould you like to:\n[1] - Restock items\n[2] - View transaction history\n[0] - Return to main menu\n>: "))
                if choice == 1 or choice == 2 or choice == 0:
                    break
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Invalid selection. Please try again.")

        if choice == 1: # restock menu
            restock_menu()
        if choice == 2: # transaction history
            transaction_log()
        if choice == 0: # return to main
            return

def restock_menu():
    while True:    
        query = "select * from items"
        item_list = db.execute(query)
        col = 0
        for i in item_list: # this for loop narrates all available items, along with the corresponding pin and stock
            pin = i[0]
            item = i[2]
            stock = i[3]
            print(f"[{pin}] {item.capitalize()} - Stock: {stock}", end=" | ")
            col += 1
            if col % 3 == 0:
                print('\n')
        while True: # this loop is used to validate the inputted pin. will keep running until user gives a valid/existing pin
            pin = input("Enter the pin of the item you want to restock\n>: ")
            pin = pin.upper()
            query = "select pin from items where pin=?;"
            if db.execute(query,[pin]).fetchone() is None:
                print("Invalid selection. Please try again.")
            else:
                break
        query = "select * from items where pin=?;"
        selected_item = db.execute(query,[pin])
        for i in selected_item: # defines the item data which is important to be used down the line
            pin = i[0]
            item = i[2]
            stock = i[3]
        while True: # loop used to validate the new stock which is inputted by the user. will deny any non-integer inputs and inputs less than or equal to 0
            try:
                added_stock = int(input(f"Selected item: {item.capitalize()}\nStock of item: {stock}\nHow much stock would you like to add?\n>: "))
                if added_stock <= 0: # exception error to make sure the inputted number is valid
                    print("Invalid amount. Ensure that the new stock is not less than or equal to 0.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please try again.")
        new_stock = stock + added_stock # returns the updated stock, given the old stock and the quantity to be added
        update_stock(new_stock,pin) # runs the function to update the stock
        print(f"Successfully updated stock! New stock of {item.capitalize()} is: {new_stock}.")
        while True: # gives users the option to restock another item
            try:
                choice = int(input(f"Would you like to restock another item?\n[1] - Yes\n[2] - No\n>: "))
                if choice == 1 or choice == 2:
                    break
                else:
                    print("Invalid input. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")
        if choice == 1: # will run another iteration of the loop
            continue
        elif choice == 2: # will end the function, asking the user if they want to go to the main menu or back to the admin panel
            while True:
                try:
                    choice = int(input("Would you like to:\n[1] - Return to admin panel\n[2] - Return to main menu\n>: "))
                    if choice == 1 or choice == 2:
                        break
                    else:
                        print("Invalid input. Please try again.")
                except ValueError:
                    print("Invalid input. Please try again.")
            if choice == 1:
                administrator_view() # goes back to admin panel
                break
            elif choice == 2:
                return # goes back to menu
            

def transaction_log():
    print(f'{'-'*20} Transaction History {'-'*20}')
    history_list = db.execute("select * from history;")
    for i in history_list: # this for loop first defines all our variables to be displayed, and displays all recorded purchases aferwards
        id = i[0] # purchase id, a unique identifier within the database
        item = i[1]
        paid_amount = i[2]
        given_change = i[3]
        purchase_date = i[4]
        print(f"[Transaction ID: {id}]\nItem purchased: {item}\nItem bought for: {paid_amount}$\nChange given: {given_change}$\nDate of purchase: {purchase_date}\n")
    while True:
        choice = input("[Type 'back' to return to the previous menu.]\n>: ")
        choice = choice.upper()
        if choice == 'BACK':
            administrator_view()
            break
        else:
            continue # simply loops back, asking once again if the user wants to go back


def purchase_action(): # function to purchase items, with the options to terminate the program or go back to the previous menu
    while True:
        pin = input(f"\n{'-'*30}\nBalance: {balance}$\n \n[Enter a PIN to purchase the corresponding item.]\n[Type 'back' to return to item selection.]\n[Type 'exit' to leave the vending machine.]\n>: ")
        pin = pin.upper()
        if pin == 'BACK': # action to go back to the previous menu
            main()
            break
        elif pin == 'EXIT': # action to terminate the program
            print("Exiting vending machine.")
            break
        else:
            query = "select pin from items where pin=?;"
            if db.execute(query,[pin]).fetchone() is None: # check if registered pin exists in the database
                print("Invalid selection. Please try again.")
            else:
                query = "select * from items where pin=?;"
                for i in db.execute(query,[pin]): # this for loop will go through the output of the executed function, because sql functions return a list, therefore, they must be interpreted within a for loop and necessary items are definedd there
                    item = i[2]
                    price = i[4]
                    stock = i[3]
                if check_stock(item) is False: # deny if item is not in stock
                    print("Transaction cannot be completed:\nItem is not in stock")
                    continue
                if balance < price: # deny if balance is not enough
                    print("Transaction cannot be completed:\nBalance is insufficient.")
                    continue
                else:

                    change = balance - price # will return the new stock after purchase
                    print(f"{item.capitalize()} purchased!\nChange given: {change}$")
                    new_stock = stock - 1 # returns the new stock number
                    update_stock(new_stock,pin) # runs the updating function which updates the stock of the item with its respective pin
                    purchase_date = datetime.datetime.now()
                    purchase_date = purchase_date.strftime("%Y/%m/%d %H:%M:%S")
                    log_purchase(item,price,change,purchase_date) # runs the logging function which adds a new entry to the 'history' table
                    break


# --------------------------- #
# data handling functions
# --------------------------- #
def update_stock(stock,pin): # function to update the stock, can be used with the purchase action task to take one away from the database
    query = "update items set stock=? where pin=?;"
    db.execute(query,(stock,pin))
    db.commit()

def check_stock(item): # function to validate if an item is in stock or not
    query = "select * from items where item=?;"
    stock = db.execute(query,[item])
    for i in stock:
        if i[3] > 0:
            return True
        else:
            return False

def display_if_stock(item,price): # function to be used in the menu, will iterate through a given item and see if the item is in stock in the database
    if check_stock(item):
        return f'{item.capitalize()} - {price}$'
    else:
        return 'Out of Stock'

def log_purchase(item,payment,change,date): # function to add purchases to the transaction log
    query = "insert into history(item,amount_paid,change_given,purchase_date) values(?,?,?,?);"
    values = (item,payment,change,date)
    db.execute(query,values)
    db.commit()

# --------------------------- #
# display functions
# --------------------------- #

# function to display all items regardless of categories
def display_all():
    general_item_list = db.execute('select * from items') # will return the raw list of all items
    col = 0
    print(f"{'-'*10} All items {'-'*10}\n")
    for i in general_item_list:
        item = i[2]
        price = i[4]
        print(f"[{i[0]}] {display_if_stock(item,price)}", end=" | ")
        col += 1
        if col % 3 == 0: # this is to make sure that the text splits after 3 entries are given, formatting the items in a 3x3 square
            print("\n")
    purchase_action() # runs the purchase action, which gives the user the option to purchase the item given the menu


# function to display items within specified category, to be chosen by the user
def display_specific():
    categories = {
        1: 'chips', 
        2: 'drinks', 
        3: 'sweets', 
    }
    while True: # a while loop is utilized here in order to validate user input, forcing the user to input a correct option
        try:
            valid_choices = [1,2,3,0] # a list which will be used to validate user input, as seen below
            category_choice = int(input("Which category would you like to view:\n[1] Chips\n[2] Drinks\n[3] Sweets\n \n[0] Previous Menu\n>: "))
            if category_choice in valid_choices: # validates the user input, checking if the given input is within the scope of the options given
                break # breaks the loop, allowing the user to proceed
            else:
                print('Invalid choice. Try again.')
        except ValueError:
            print('Invalid choice. Try again.')

    if category_choice == 0: # returns the user to the main menu if the option is chosen
        main()
    else: # a simple else condition is used because the input was already validated prior to  this in the while loop, therefore we do not need to check if the input is 1, 2 or 3
        selected_category = categories[category_choice] # calls the dictionary given earlier in the script with the respective number, giving the uesr the category they chose
        query = 'select * from items where category =?'
        selected_category_list = db.execute(query,[selected_category])  # sql function which will list out all items with the given category
        print(f"{'-'*10} Items in {selected_category.capitalize()} Category {'-'*10}\n")
        for i in selected_category_list:
            item = i[2]
            price = i[4]
            print(f"[{i[0]}] {display_if_stock(item,price)}", end=" | ")
        print('\n')
        purchase_action()


# --------------------------- #
# MAIN
# --------------------------- #


administrator_check()
while True: # a while loop is used again to ensure that a valid balance is given by the user
    try:
        balance = int(input("Thank you for using this vending machine!\nPlease input your balance:\n>: $"))
        if balance <= 0:
            print('Balance cannot be less than or equal to 0. Try again.')
        elif balance > 100:
            print('Given balance is too large. Maximum balance: 100')
        else:
            break
    except Exception:
        print('Invalid balance. Try again.')
main()
