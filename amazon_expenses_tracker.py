import re
import time
import datetime
import getpass
import sys


def password_checker(password):
    '''function to check if entered password matches given critera:
    Should have at least one number.
    Should have at least one uppercase and one lowercase character.
    Should have at least one special symbol.
    Should be between 6 to 20 characters long.
    '''
    valid_pw = re.compile("^(?=.*\\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[@&%!?$_])[\\da-zA-Z@&%!?$_]{6,20}$")
    if re.search(valid_pw, password):
       return True 
    return False
    
def valid_number(phone_number):
    '''function to check if a phone number is a german cellphone number'''
    if re.search("^(\\+|00)(49)[\\d]{8,15}$", phone_number):
       return True 
    return False
#log in screen, ask for name + password and check for match
# 3 attempts then delay for 5 seconds, exit program if wrong again.
def login():
    '''function that takes login info and checks if it's valid'''
    
    print("To log in please enter your name and password.")
    name = input("Name: ").title()
    pwd = getpass.getpass()
    if name == username and pwd == password:
        print("Successfully logged in.")
        time.sleep(1)
        print("Welcome to the Amazon Expense Tracker!")
        return True
    elif name != username:
        if pwd != password:
            print("Login failed.")
            return False
        print("Invalid username. Login failed.")
        return False
    elif pwd != password:
        print("Invalid password. Login failed")
        return False
   



#registration and log in 

#take username, password and phone number  
phone_number = None
username = input("Enter Name to register:\n>").title()
print("Password should be between 6 to 20 characters long and have at least one of each: a number, uppercase and lowercase character, special symbol(@&%!?$_).")


password = getpass.getpass()
if not password_checker(password):
    print("Try again.")
    sys.exit()
    
else:
    print("Valid password.")
        
 
    
    while phone_number == None:
        phone_number = input("Enter a German phone number:\n>")
        if not valid_number(phone_number):
            print("Not valid.")
            phone_number = None
        else:
            print("Registration successful.")
        #three attempts to login
            time.sleep(1)
            print("LOGIN SCREEN")
            login_attempts = 0
            for _ in range(3):
                if login():
                    break
                else:
                    login_attempts +=1
            if login_attempts >=3:
                print("Max. attempts reached. Wait 5 seconds to try again.")
                time.sleep(5)
                if not login():
                    print("Try again later.")
                    sys.exit()
                else:
                    print("Login successful.")


#start of main program

#epurchase tracker with dictionary function 
#take user input in purchase_tracker function and store list of dictionaires



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
        purchase_date = input("Enter Date of purchase (MM/DD/YYYY or MM-DD-YYYY) or enter 'today' for today's purchases:\n—>  ").lower()
        if purchase_date == "today":
            purchase_date = today.strftime("%m/%d/%Y")
        if not valid_date(purchase_date):
            print("Invalid Format. Reminder: MM/DD/YYYY or MM-DD-YYYY")
            purchase_date = None
        else:
            items["Date of purchase"] = save_date(purchase_date)
            
            
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
    

def report(purchases):
    #get total weight from purchases 1kg = 1€ shipping
    #get total cost, subtract weight from total
    #calculate most expensive and least expensive purchase
    #calculate average cost per purchase
    #check if spending limit has been exceeded
    
    item = [items.get("Item") for items in purchases if "Item" in items]
    cost = [items.get("Price") for items in purchases if "Price" in items]
    weight = [items.get("Weight") for items in purchases if "Weight" in items]
    date = [items.get("Date of purchase") for items in purchases if "Date of purchase" in items]

    total_cost = sum(cost)
    shipping_cost = sum(weight)
    item_cost = total_cost - shipping_cost
    average_cost = total_cost / len(cost)
    highest_cost = max(cost)
    highest_cost_item = item[cost.index(highest_cost)]
    date_high = date[cost.index(highest_cost)] 
    lowest_cost = min(cost)
    lowest_cost_item = item[cost.index(lowest_cost)]
    date_low = date[cost.index(lowest_cost)]
    spending_limit = 500
    overdraw = total_cost - spending_limit
    today = datetime.date.today()
   
   #generating report 
   #
     
    print("...generating report") 
    time.sleep(1)
    print("   ...")
    time.sleep(1)
    print("     ...") 
    time.sleep(1)
    print("       ...") 
    time.sleep(1)
    
    #print name + data 
    #printing expense report
    
    print("*********************************************")
    print("*                                           *")
    print("*             Expenses Report:              *")
    print("*                                           *")
    print("*********************************************")
    print("")
    print(f"                                   {today.strftime("%m/%d/%Y")}")
    print("")
    print(f"     | Name: {username} | Phone No.:{phone_number}| ")
    print("      ——————————————————————————————————")
    print("      |      Expenses Overview         |")
    print("      ——————————————————————————————————")
    print(f"      Total Shipping Cost —> {shipping_cost:.2f}€")
    print(f"      Total Item Cost —>  {item_cost:.2f}€")
    print(f"      Total Cost —>  {total_cost:.2f}€")
    print("")
    print(f"      Average Cost per Item —> {average_cost:.2f}€")
    print(f"      Most expensive item: {highest_cost_item}")
    print(f"      —> {highest_cost:.2f}€ on {date_high}")
    print(f"      Cheapest item: {lowest_cost_item}")
    print(f"      —> {lowest_cost:.2f}€ on {date_low}")
    print("")
    
    if total_cost < spending_limit:
        print(f"Budget of {spending_limit}€ has not been exceeded.")
    else:
         print(f"Budget of {spending_limit}€ has been exceeded by {overdraw:.2f}€")
   
    
#print menu that prompts user for 3 options

running = True

purchases = []
#items = {}
today = datetime.date.today()
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

  
    option = input("Enter your option (1 to 3):\n—> ").lower()
    
    while option not in (["1", "2", "3"]):
        print("Invalid. Try again.")
        option = input(" > Enter your option (1 to 3):\n—> ").lower()
    
    if option == "1":
        purchase_tracker()
        time.sleep(1)
        #print(purchases) #testing
        
    elif option == "2":
        try:
            report(purchases)
            time.sleep(5)
        except ZeroDivisionError:
            print("No purchase data has been stored.")
            time.sleep(1)
            
        
        
        
    elif option == "3":
        print("Goodbye.")
        sys.exit()

