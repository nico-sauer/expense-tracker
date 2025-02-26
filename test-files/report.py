#report generator hard-coded for testing first 

import datetime
import time
purchases = [
    {'Item': 'Book', 'Date of purchase': '02/09/2025', 'Price': 12.0, 'Weight': 1.0, 'Quantity': 3},
    {'Item': 'Lego', 'Date of purchase': '02/02/2025', 'Price': 500.0, 'Weight': 2.0, 'Quantity': 1},
    {'Item': 'Video Game', 'Date of purchase': '02/02/2025', 'Price': 75.0, 'Weight': 1.0, 'Quantity': 1},
    {'Item': 'More books', 'Date of purchase': '02/07/2025', 'Price': 20.5, 'Weight': 3.5, 'Quantity': 5}]


username = "Nico"
phone_number = "0123456789"
today = datetime.date.today()
purchases = [
    {'Item': 'Book', 'Date of purchase': '02/09/2025', 'Price': 12.0, 'Weight': 1.0, 'Quantity': 3},
    {'Item': 'Lego', 'Date of purchase': '02/02/2025', 'Price': 500.0, 'Weight': 2.0, 'Quantity': 1},
    {'Item': 'Video Game', 'Date of purchase': '02/02/2025', 'Price': 75.0, 'Weight': 1.0, 'Quantity': 1},
    {'Item': 'More books', 'Date of purchase': '02/07/2025', 'Price': 20.5, 'Weight': 3.5, 'Quantity': 5}]

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
    '''
     
    print("...generating report") 
    time.sleep(1)
    print("   ...")
    time.sleep(1)
    print("     ...") 
    time.sleep(1)
    print("       ...") 
    time.sleep(1)
    '''
    
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
report(purchases)
   