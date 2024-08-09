import csv
from datetime import datetime
import schedule
import time

# Function to read excluded dates from a CSV file
def get_excluded_dates(csv_file):
    print("Print 1")
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        excluded_dates = [row[0] for row in reader]
    return excluded_dates

# Function to check if today's date is in the excluded dates
def is_excluded_date(excluded_dates):
    print("Print 2")
    today = datetime.now().strftime('%Y-%m-%d')
    return today in excluded_dates

# Function to check if today is a weekday (Monday to Friday)
def is_weekday():
    print("Print 3")
    today = datetime.now().weekday()  # 0 = Monday, 6 = Sunday
    return today < 5  # Monday to Friday are considered weekdays

# The job to be scheduled
def joblogout():
    print("Print 4")
    excluded_dates = get_excluded_dates('excluded_dates.csv')
    if is_weekday() and not is_excluded_date(excluded_dates):
        exec(open("/home/abp/Documents/Automate/LogOut.py").read())

# The job to be scheduled
def joblogin():
    print("Print 5")
    excluded_dates = get_excluded_dates('excluded_dates.csv')
    if is_weekday() and not is_excluded_date(excluded_dates):
        exec(open("/home/abp/Documents/Automate/LogIn.py").read())

# Schedule the job at 10 AM and 8 PM daily
schedule.every().day.at("16:17").do(joblogin)
print("Print 6")
schedule.every().day.at("16:16").do(joblogout)
print("Print 7")

# Main loop to keep the schedule running
while True:
    schedule.run_pending()
    time.sleep(1)