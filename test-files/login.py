# only the registration + login part of the code

import re
import time

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
    name = input("Name: ")
    pwd = input("Password: ")
    if name == username and pwd == password:
        print("Successfully logged in.")
        time.sleep(1)
        print("Welcome to the Amazon Expense Tracker!")
        return True
    elif name != username:
        print("Invalid username.")
        return False
    elif pwd != password:
        print("Invalid password.")
        return False



#main code begins here

#take username, password and phone number  

username = input("Enter Name to register:\n>")
print("Password should be between 6 to 20 characters long and have at least one of each: a number, uppercase and lowercase character, special symbol(@&%!?$_).")

password = input("Enter a password: ")
if not password_checker(password):
    print("Try again.")
    
else:
    print("Successful password.")
        
    phone_number = None 
    
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
                else:
                    pass
            