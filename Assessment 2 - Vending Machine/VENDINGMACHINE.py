import sys # For exiting console because exit() doesn't work.
import time # Adding delay.
cost = 0 # Stores the cost of the products.
bill = [] # Stores the ID of the products.
itemdata = { # Nested Dictionary, with two categories, storing the name, ID and price.
    "Drinks (A)" : {
        "A1" : {"itemName" : 'Water', "itemPrice" : 1.00},
        "A2" : {"itemName" : 'Kold Koffee', "itemPrice" : 3.00},
        "A3" : {"itemName" : 'NRGY', "itemPrice" : 5.00},
        "A4" : {"itemName" : 'Soda Pop', "itemPrice" : 5.00}
        },
    "Snacks (B)" : {
        "B1" : {"itemName" : 'Chokkolate', "itemPrice" : 3.50},
        "B2" : {"itemName" : 'Chip-pers', "itemPrice" : 5.00},
        "B3" : {"itemName" : 'Biscuits', "itemPrice" : 2.50},
        "B4" : {"itemName" : 'Kool Kandy',"itemPrice" : 4.50}
        },
}
def displayMenu(cost): # Created a function that displays the menu with the drinks and snacks, and has global variable.
    print("\n--- Welcome to the Vending Machine! ---")
    print(f"Current Total Cost: ${cost:.2f}") # This prints, using variable 'cost', the total current cost to the user.
    print("Here are the available categories:")
    
    for menu, items in itemdata.items(): # for loop that accesses the nested items.
        print(f"\n{menu}:") # Accesses the first information stored into the dictionary and prints it, that being 'Drinks' and 'Snacks'.

        for itemdetails in items.values(): # An indented for loop that retrieves the values inside items. It skips the ID, and accesses the information nested after.
            print(f"- {itemdetails['itemName']}") # Accesses the item names that is nested after ID and prints it, using f" to fill the information, and separating each information with -
           
def displayDrinks(itemdata): # Created a function that displays the Drink category. Global variable is the dictionary.
    print("Available Drinks:")
    
    drinks = itemdata["Drinks (A)"] # Variable made to only access the Drinks category of the dictionary.

    for itemid, itemdetails in drinks.items(): # For loop that accesses the ID and other details in Drinks.
        itemname = itemdetails['itemName'] # Variable that accesses the dictionary to get the name.
        itemprice = itemdetails['itemPrice'] # Variable that accesses the dictionary to get the price.
        print(f"- {itemname}: ID: {itemid} | Price: ${itemprice}") # Using f" to fill in the information, separating the name, ID and Price, and prints.

def displaySnacks(itemdata): # This is pretty much the same as the display drinks.
    print("Available Snacks:")
    
    snacks = itemdata["Snacks (B)"] # This accesses the snacks instead of the drinks dictionary.

    for itemid, itemdetails in snacks.items():
        itemname = itemdetails['itemName']
        itemprice = itemdetails['itemPrice']
        print(f"- {itemname}: ID: {itemid} | Price: ${itemprice}")


def buyDrinks(itemdata): # Function created to ask and act if the user wants to buy drinks in the drinks category
    global cost # Using global variable instead of putting it inside the function because it breaks some of the code and prevents it from working.
    global bill
    while True:
        buyA = input("Enter the ID of the item you want to buy: (Type 'back' to go back) ") # User input question that tells the user to enter the ID of the item they want to buy.
        if buyA == 'back': # If function to check if the user inputs 'back' into the user input.
            displayMenu(cost)
            main()
            # ^ This sends the user back to the display menu and main function area.
            break
        
        correctID = False # Variable made to check if ID inputted exists in table.
        
        for itemid, itemdetails in itemdata["Drinks (A)"].items(): # For loop that accesses Drinks dictionary.
            if itemid == buyA: # If function that efficiently checks if the itemID exists from the user input is true.
                price = itemdetails["itemPrice"] # Variable that accesses the item's price.
                cost += price # This adds the item's price into the global variable 'cost'.
                bill.append(buyA) # Adds the user inputted ID into the front of the variable 'bill', thus why append is used.
                print(f"Purchased {itemdetails['itemName']} for ${itemdetails['itemPrice']}. Total Cost: ${cost:.2f}") # Using f" to fill the information that tells the user what they purchased for how much, then displays the total cost of everything they have bought.
                correctID = True # Sets the variable to true as the if statement is true.
                time.sleep(2) # Delay for aesthetic purposes
                break # Breaks the if loop, allowing the buyA variable to loop.
            
        if not correctID: # Checks for opposite condition, where it checks if the correctID is true.
            print("Invalid Input!") # Tells the user the ID they inputted is invalid
            buyA = str(input("Enter any key to continue: ")) # Changes the buyA variable in order to restart the loop.
        


# The buySnacks is the same as buyDrinks. Only the dictionary changed.
def buySnacks(itemdata):
    global cost
    global bill
    while True:
        buyB = input("Enter the ID of the item you want to buy: (Type 'back' to go back) ")
        if buyB == 'back':
            displayMenu(cost)
            main()
            break
        
        correctID = False
        
        for itemid, itemdetails in itemdata["Snacks (B)"].items():    
            if itemid == buyB:
                price = itemdetails["itemPrice"]
                cost += price
                bill.append(buyB)
                print(f"Purchased {itemdetails['itemName']} for ${itemdetails['itemPrice']}. Total Cost: ${cost:.2f}")       
                correctID = True
                time.sleep(2)
                break
            
        if not correctID:
            print("Invalid Input!")
            buyB = str(input("Enter any key to continue: "))


        

def main(): # Main interface in which the user is able to access the other functions of the vending machine
    while True: # while loop that will repeat if an input is invalid.
        dors = input("Which menu would you like to view? A/B (Type 'PAY' to pay for your bill) ").casefold() # Asks for user input whether to check the categories or pay.
        if dors=="A".casefold(): # Checks if input is A, which is the Drinks category
            print("Loading...") # Aesthetic
            time.sleep(1)
            displayDrinks(itemdata) # Opens the drink category
            time.sleep(1)
            buyDrinks(itemdata) # displays the input question to the user
            break # Stops the loop
        
        elif dors=="B".casefold(): # ^ Same is applied here from above, just checks if it is snacks instead.
            print("Loading...")
            time.sleep(1)
            displaySnacks(itemdata)
            time.sleep(1)
            buySnacks(itemdata)
            break
        
        elif dors == 'PAY'.casefold(): # Checks if user would like to pay instead
            displayBill(itemdata, bill) # Displays the bill function
            break # Stops loop
        
        else: # Else in case the user inputs an invalid input
            print("Invalid Menu!") # Tells the user
            dors = str(input("Enter any key to continue: ")) # used to restart the loop
            

    else:
        sys.exit() # Not sure why this is here, it doesn't change anything nor does it affect any of the code. I'm going to leave it here IN CASE it does but it's apparently exiting cus the user inputs so?
        
def displayBill(itemdata, bill): # Payment and bill function is made here
    if not bill: # Checks for the opposite condition, in which case, the bill is empty.
        print("Your bill is empty.") # Tells the user
        time.sleep(2)
        main() # Returns to the main function
        return # stops this function

    print("\n--- Bill Summary ---")
    totalcost = 0 # Stores the cost of the ID stored in the bill variable

    for item_id in bill: # This for loop is to check the price since the bill variable stores the ID.
        for category in itemdata.values(): # category variable to check the dictionary values
            if item_id in category: # checks if item ID is inside the dictionary values
                item_name = category[item_id]['itemName'] # variable name is obtained from itemName
                item_price = category[item_id]['itemPrice'] # variable price is obtained from itemPrice
                totalcost += item_price # the item price is added into total cost variable
                print(f"{item_name}: ${item_price:.2f}") # Using f", it fills the information of the name and price of the item corresponding to the ID in the bill variable
                
    print(f"\nTotal Cost: ${totalcost:.2f}") # prints the total cost with 2 decimal points
    
    
    
    pay = float(input("Input your payment (Format is 00.00 add decimal when necessary): ")) # Tells the user to input their payment, and also provides reference to the decimal format.
          
    change = pay - totalcost # change variable minuses the total cost from the pay

    if pay >= totalcost: # checks if the input is more than or equal to the total cost variable
        print(f"You have paid ${pay}") # tells the user how much they have paid by filling in the information
        print("Your change is $",change) # tells the user their change using the change variable
        time.sleep(1)
        print("Thank you for your purchase!") # Thanks the user
        time.sleep(1)
        print("See you again soon!") # See you again by Tyler, The Creator (Or Wiz Khalifa, depends on what you listened to first)
        return
            
             
    elif pay < totalcost: # Checks if the pay is less than the total cost
        print("Not enough money inputted.") # Tells the user that they're broke
        time.sleep(2)
        print("Try again.") # Try again
        time.sleep(2)
        displayBill(itemdata, bill) # Displays the bill once more and loops it
    

# Wow, very cool ascii art of a vending machine

print("""
        ⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛
       ⣿    VENDING MACHINE     ⣿
⠀      ⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡿⠿⢿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⢠⣤⠀⠀⣴⠀⠀⠀⠀⠀  ⣿⠀⣶⠀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠰⠾⠿⠶⠾⠿⠶⠶⠶⠶⠀⣿⣀⣉⣀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀  ⣿⣏⣉⣹⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠐⠒⠒⠒⠒⠒⠚⠛⠓⠒⠀⣿⣯⣉⣹⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⢠⡀⠀⣾⠀⠀⣶⡆⠀⠀ ⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⣶⣦⠀⣶⣶⠀⠀⠀⠀⠀ ⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⣿⣏⣉⣹⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
""")
print("""You come across a vending machine.""") # No way, vending machine
time.sleep(2)
start = input("Would you like to use the vending machine? Y/N ").casefold() # No

if start == "Y".casefold(): # Checks if user inputted Y
    print("Loading...")
    time.sleep(2)
    displayMenu(cost) # 
    main()
    
    # where did my N go 💀? It's fine, it works normal if you do N, it'll exit anyways.
    
# I got everything important done.
# •	A menu of drinks and snacks presented via the console. The number and range of items is up to you. ✅
# •	A set of numbers or codes that the user can input to select a particular drink or snack. ✅
# •	A way of managing money so the user can input any amount of money and have the correct change returned. ✅
# •	A message that tells the user that a particular drink or snack has been dispensed. ✅
# •	 A message that tells the user how much change they have received. ✅
# •	 Comments in the code to explain key operations. ✅ (I did comments on nearly everything though but it's fine.)

# As for additional ones as stated in the document.
# •	A method of categorising items in the vending machine to improve the user experience (e.g. ‘Chocolate’ or ‘Hot Drinks’). ✅ (Drinks and Snacks, that's it)
# •	A way of allowing users to buy additional items. ✅
# •	Appropriate error checking to validate inputs and ensure the user has enough money 🟡 (Erm, I did for majority of them. Few just won't work)
# •	An intelligence system for suggesting purchases. For example, if you buy a coffee, the vending machine may suggest that you buy biscuits. ❌ (no.)
# •	A stock system meaning the machine may run out of products. ❌  (Absolutely not. I could, but I am too lazy.)


# That is all, folks, I shall document now.

    





        
        
    