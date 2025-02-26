#payment reminder
import re
import datetime
from datetime import timedelta
from datetime import datetime
def payment_reminder():
    print("***********************")
    print("*                     *")
    print("*  Payment Reminder:  *")
    print("*                     *")
    print("***********************")
    reminder = None
    while reminder == None:
        reminder = input("Enter payment due date (MM/DD/YYYY or MM-DD-YYYY)\n—>")
        if not valid_date(reminder):
            print("Invalid Format. Reminder: MM/DD/YYYY or MM-DD-YYYY")
            reminder = None
        else:
            time = None
            while time == None:
                try:
                    time = int(input("Select reminder alert 1, 2 or 3 days before the payment is due\n—>"))
                    reminder = re.sub("/", "-", reminder)
                    reminder = datetime.strptime(reminder, '%m-%d-%Y')
                    reminder = reminder - timedelta(time)
                    reminder = datetime.strftime(reminder, '%m-%d-%Y')
                    reminder = re.sub("-", "/", reminder)
                    print("Reminder set for:", reminder)
                except ValueError:
                    time = None
def valid_date(str):
    '''function to validate given date format'''
    if re.match(r"^(0[1-9]|1[1,2])(\/|-)(0[1-9]|[12][0-9]|3[01])(\/|-)(19|20)\d{2}$", str):
        return True
    return False

payment_reminder()