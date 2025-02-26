#epurchase tracker with dictionary function 
#take user input in purchase_tracker function and store in list/dictionary (list of dictionaires?)

import re
import datetime
import numbers
def purchase_tracker():
    print("***********************")
    print("*                     *")
    print("*  Purchase Tracker:  *")
    print("*                     *")
    print("***********************")
    items = {}
    # ask for item name until it matches criteria
    item_name = "" 
    while len(item_name) <= 3:
        item_name = input("Enter purchased item (min. 3 letters):\n—> ").title()
        items["Item"] = item_name
    
    
    #ask for purchase date until valid input + change to desired format
    purchase_date = None

    while purchase_date == None:
        purchase_date = input("Enter Date of purchase (MM/DD/YYYY or MM-DD-YYYY):\n—>  ")
        if not valid_date(purchase_date):
            print("Invalid Format. Reminder: MM/DD/YYYY or MM-DD-YYYY")
            purchase_date = None
        else:
            items["Date of purchase"] = save_date(purchase_date)
            #print(save_date(purchase_date)) # for testing remove later
            
    #ask for item cost until it matches critera
    purchase_cost = None
    while purchase_cost == None:
        try:
            purchase_cost = float(input("Enter item price in Euro\n—> "))
            items["Price"] = purchase_cost
            #print("valid input") #test change later
        except ValueError:
            purchase_cost = None

    #ask for item weight until it matches criteria
    item_weight = None  
    while item_weight == None:
        try: 
            item_weight = float(input("Enter item weight in kg:\n—> "))
            items["Weight"] = item_weight
            #print("valid input") #for testing change later
        except ValueError:
            item_weight = None
        
    #ask for purchase quantity until it matches criteria
    purchase_quantity = None
    while purchase_quantity == None:
        try:
            purchase_quantity = int(input("Enter purchased quantity:\n—> "))
            items["Quantity"] = purchase_quantity
            #print("valid input") #testing change later
        except ValueError:
            purchase_quantity = None

        
        purchases.append(items)
        print("Purchase saved.")
    


def save_date(purchase_date):
    '''function to standardize format of given valid purchase date'''
    purchase_date = re.sub("-", "/", purchase_date)
    return purchase_date
    
def valid_date(purchase_date):
    '''function to validate given purchase date format'''
    if re.match(r"^(0[1-9]|1[1,2])(\/|-)(0[1-9]|[12][0-9]|3[01])(\/|-)(19|20)\d{2}$", purchase_date):
        return True
    return False
    


   
    
#print menu that prompts user for 3 options

running = True
#empty list and dictionary
purchases = []
#items = {}
 
while True:
    print("***********************************")
    print("*              ***                *")
    print("*         Welcome to the          *")
    print("*     Amazon Expense Tracker!     *")
    print("*              ***                *")
    print("***********************************")
    print("")
    print(" >>> Menu Options:")
    print("  > 1. Enter a purchase.")
    print("  > 2. Generate report.")
    print("  > 3. Quit")

  
    option = input("Enter your option (1 to 3) or 'x' to quit:\n—> ").lower()
    
    while option not in (["1", "2", "3"]):
        print("Invalid. Try again.")
        option = input(" > Enter your option (1 to 3) or 'x' to quit:\n—> ").lower()
    
    if option == "1":
        purchase_tracker()
        #print(purchases) #testing
        
    elif option == "2":
        print("This option is not available yet!")
        
        
    elif option == "3":
        print("Goodbye.")
        break
        
        #sys.exit()

     
