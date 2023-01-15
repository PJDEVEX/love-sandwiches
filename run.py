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

# Access data in sales sheet
data = sales.get_all_values()


print(data)