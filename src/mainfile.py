import time
import Security
import IO
import objs
from objs import cart

user_name = []
pass_word = []
billing_address = []
card_number = []

def main():
    for x in range(50):
        print("")
    print("Hello! Welcome to _____ Emporium where we sell all kinds of instruments")
    print("Please! Choose 1 of the following options based on what you would like to do.")
    print("1. Login to Account")
    print("2. Create Account")
    print("Any other Number: Close application")
    user_choice = input("Please enter 1, 2, or any number: ")

    if user_choice == '1':
        login_function()
    elif user_choice == '2':
        account_create_function()
    else:
        print("The program will now shutdown. Thank you for your continued patronage and have a nice day")
        time.sleep(5)
        quit()

def login_function():
    for x in range(50):
        print("")

    user_name = input("Please enter your username: ")
    pass_word = input("Please enter your password: ")

    if Security.validateUser(user_name,pass_word):
        print("You are being logged in to your account!")
        time.sleep(5)
        main_menu_function()
    else:
        print("Your username and password did not match our database. Please re-enter them.")
        login_function()    

def account_create_function():
    for x in range(50):
        print("")

    global user_name
    user_name = input("Please choose a username: ")

    global pass_word
    pass_word = input("Please enter a password that is 8 characters long: ")

    if len(pass_word) < 8:
        while len(pass_word) < 8:
            pass_word = input("Your password was not 8 characters long at aminimum. Please try again: ")

    global email_new
    global phone_number
    global billing_address
    global debit_card_number

    email_new = input("Please enter an email address: ")
    phone_number = input("PLease enter your phone number: ")
    billing_address = input("Please enter your billing address: ")    
    debit_card_number = input("Please enter a FAKE 16 digit debit card number: ")
    
    IO.addUserEntryByObj(IO.User(IO.getUserKey(),user_name,Security.hash(pass_word),billing_address,email_new,phone_number,debit_card_number))
    print("Thank you for creating an account. We will now transport you back to the login menu so that you can log in to your new account!")
    time.sleep(5)

    main()
    
def main_menu_function():
    for x in range(50):
        print("")

    print("Thank you for logging in and your continued patronage is appreciated.")
    print("There are several options you can do now. You like to shop for items, view your cart, edit personal info, or logout(Closing the application)")
    print("1. Shop for Instruments")
    print("2. View Cart")
    print("3. Edit Personal Information")
    print("Any other number: Logoff")

    menu_choice = input("Please enter one of the numbers above: ")

    if menu_choice == '1':
        shopping_function()
    elif menu_choice == '2':
        view_cart_function()
    elif menu_choice == '3':
        personal_info_function()
    else:
        print("Thank you for shopping with us! We will now log you out!")
        time.sleep(5)
        quit()

def shopping_function():
    for x in range(50):
        print("")

    print("Welcome to our online shop!")
    print("We will now provide a categorized list of items you can purchase")
    print("In order from left to right each column is:")
    print("ID Number, Item Name, Price in Dollars, Category, Inventory Amount")
    print("********************************************************************")

    items = IO.getItems()

    for item in items:
        print(item.toString())
    print("")
    user_choice = input("If you would like to shop for items, please press 1: ")
    while user_choice == '1':
        shop_choice = input("Please choose an item from the above list: ")
        IO.addCartEntryByObj(IO.Cart(Security.getUserID(),shop_choice,1))
        user_choice = input("If you would like to purchase another item, please press 1: ")
        if user_choice is not '1':
            print("You will now be returned to the main menu!")
            time.sleep(5)
            break
    main_menu_function()

def view_cart_function():
    for x in range(50):
        print("")

    print("Welcome to the cart menu!")
    print("Here you can access your cart, checkout, and many other things.")
    print("1. Display Items in cart.")
    print("2. Remove Item from cart.")
    print("3. View Previous orders.")
    print("4. Checkout!")
    print("Any other Number. Return to Main menu")

    user_choice = input("If you would like to access one of these options please press 1: ")

    while user_choice == '1':
        user_menu_choice = input("Which option would you like to choose? Please press 1, or any number listed above: ")
        if user_menu_choice == '1':
            display_cart_function()
        elif user_menu_choice == '2':
            remove_item_function()
        elif user_menu_choice == '3':
            view_orders_function()
        elif user_menu_choice == '4':
            checkout_function()
        else:
            print("You will now be returned to the main menu.")
            time.sleep(5)
            break
        user_menu_choice = input("Would you like to choose another option? If so, please press 1: ")
    main_menu_function()
    
def display_cart_function():
    for x in range(50):
        print("")

    print("I have made a list of the current items in your cart.")
    carts = IO.getCarts()
    for cart in carts:
        if cart.getUserID() == Security.getUserID():
            print(cart.toString())
    user_choice = input("Please press 1 when you would like to return to the main menu! ")

    while True:
        if user_choice == '1':
            print("You will now be returned to the main menu!")
            time.sleep(5)
            break
        else:
            print("You did not press 1. Please press 1 to return to the main menu.")
            print("")
            user_choice = input("Please press 1 when you would like to return to the main menu!  ")
    main_menu_function()
    
def remove_item_function():
    for x in range(50):
        print("")

    print("Here is a list of your current items.")
    print("From left to right columnwise we have: ")
    print("Your secure UserID, ItemID, and the Quantity")

    carts = IO.getCarts()
    for cart in carts:
        if cart.getUserID() == Security.getUserID():
            print(cart.toString())

    user_choice = input("If you would like to choose an item to remove, please press 1: ")

    while user_choice == '1':
        remove_item = input("Please enter the number of the item you wish to remove. If you do not want to remove any more items please press a number not labled in your cart: ")

        if int(remove_item) < 26:
            #NEED TO REMOVE ITEMS FROM CART
            carts = IO.getCarts()
            updated_carts = []
            for cart in carts:
                if cart.getUserID() != Security.getUserID() and remove_item != cart.getItemID():
                    updated_carts.append(carts)
            IO.writeCarts(updated_carts)                    
            print("The item has been removed!")
        else:
            print("We will assume that you do not want to remove any more items from your cart and we will now send you back to the main menu.")
            time.sleep(5)
            break

        user_choice = input("If you would like to remove another item, please press 1: ")

    print("Your items have been successfully removed from your cart. We will now send you back to the main menu!")
    time.sleep(5)
    main_menu_function()
    

def view_orders_function():
    print("previous orders here")

    for x in range(50):
        print("")

    print("Here is a list of your previous orders!")

    for purchase in IO.getPurchases():
        if purchase.getUserID() == Security.getUserID():
            print(purchase)

    print("You will now be sent back to the main menu! Thank you for your continued patronage!")
    time.sleep(5)
    main_menu_function()

def cart_checkout_function():
    print("I have made a list of the current items in your cart.")
    print("")

    carts = IO.getCarts()
    for cart in carts:
        if cart.getUserID() == Security.getUserID():
            print(cart.toString())

def checkout_function():
    print("checkout menu things")

    for x in range(50):
        print("")

    print("Welcome to the checkout page!")
    cart_checkout_function()
    
    currentAddressToPrint = ""
    currentCardToPrint = ""

    for user in IO.getUsers():
        if user.getID() == Security.getUserID():
            currentAddressToPrint = user.getAddress()
            currentCardToPrint = user.getCreditCard()
            break

    print("Address:",currentAddressToPrint)
    print("Card number:",currentCardToPrint)

    user_card_number = input("Is this card number correct? Press 1 if it is: ")
    if user_card_number != '1':
        print("We are very sorry to hear that we had your information stored incorrectly. Could you please tell us the correct card number?")
        while True:
            user_card = input("Please type 1 to change your card number associated with your account: ")
            if user_card == '1':
                card_number = input("Please enter your correct card number that you would like associated with your account: ")

                users = IO.getUsers()

                for user in users:
                    if user.getID() == Security.getUserID():
                        user.setCreditCard(card_number)
                        break

                IO.writeUsers(users)

                break
            else:
                print("We will assume that your card information is now correct. Thank you for giving us this information!")
                break
    print("Here is your order! Please confirm that it is correct!")

    runningPrice = 0.0

    for cart in IO.getCarts():
        if cart.getUserID() == Security.getUserID():
            print(cart)
            for item in IO.getItems():
                if item.getID() == cart.getItemID():
                    runningPrice = runningPrice + (item.getPrice() * cart.getQuantity())

    print("Total cost: $",runningPrice)

    user_third_choice = input("Please press 1 to confirm that your order is correct: ")
    if user_third_choice != 1:
        print("We will now reroute you to the main menu. From there you can go to the shopping area or open up the cart area so that you can remove items")
        time.sleep(5)
        main_menu_function()
    print("Your order has been placed! Thank you for your patronage, and we will now reroute you to the main menu!")

    #remove all items from cart with user id
    #move those to purhcase and add a time to it
    #subtract the inventory from items.csv

    time.sleep(5)
    main_menu_function()

def personal_info_function():
    for x in range(50):
        print("")

    print("Time to update your personal information.")
    print("Please! Choose 1 of the following options based on what information you would like to update.")
    print("1. Username")
    print("2. Password")
    print("3. Email")
    print("4. Billing Address")
    print("5. Payment Info")
    print("Any other Number: Back to the Main Menu")

    user_if_change = input("If you would like to change something please press 1. If you do not want anything changed press any number besides 1: ")

    while user_if_change == '1':
        user_choice = input("Please enter 1, 2, or any number above: ")
        if user_choice == '1':
            username_new = input("Please enter a new username: ")

            users = IO.getUsers()

            for user in users:
                if user.getID() == Security.getUserID():
                    user.setName(username_new)
                    break

            IO.writeUsers(users)

        elif user_choice == '2':
            password_new = input("Please enter a new password: ")
            
            users = IO.getUsers()

            for user in users:
                if user.getID() == Security.getUserID():
                    user.setPassword(Security.hash(password_new))
                    break

            IO.writeUsers(users)

        elif user_choice == '3':
            email = input("Please enter a new email: ")
            
            users = IO.getUsers()

            for user in users:
                if user.getID() == Security.getUserID():
                    user.setEmail(email)
                    break

            IO.writeUsers(users)

        elif user_choice == '4':
            billing_address = input("Please enter a new billing address: ")
            
            users = IO.getUsers()

            for user in users:
                if user.getID() == Security.getUserID():
                    user.setAddress(billing_address)
                    break

            IO.writeUsers(users)

        elif user_choice == '5':
            debit_card_number = input("Please enter new payment information: ")
            
            users = IO.getUsers()

            for user in users:
                if user.getID() == Security.getUserID():
                    user.setCreditCard(debit_card_number)
                    break

            IO.writeUsers(users)

        else:
            print("You will now be transferred back to the Main Menu!")
            time.sleep(5)
            break
        user_if_change = input("If you would like to change something else, please press 1: ")
    main_menu_function()

if __name__ == "__main__":
    main()