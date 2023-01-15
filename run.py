# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#  import the whole library
import gspread
#  improt only creadential class
from google.oauth2.service_account import Credentials

# set the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# create creds variable
CREDS = Credentials.from_service_account_file('creds.json')

# Create SCOPED_CREDS
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# Create GSPREAD_CLIENT
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# Access google sheet
SHEET = GSPREAD_CLIENT.open('love_sandwiches')
# Add data sheet          
sales = SHEET.worksheet('sales')


def get_sales_data():
    """
    Get sales figures from the user
    """
    print("Please enter sales data from the last market")
    print("Data should be six numbers, seperated by commas")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here:")
    print(f"The data provided is {data_str}")

get_sales_data()
