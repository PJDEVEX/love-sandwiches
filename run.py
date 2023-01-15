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
    Get sales figures from the user.
    Run a while loop to collect a valid string of data from user
    via the terminal, which must be a string of 6 int seperated 
    by commas. The loop will request data, until it is valid.
    """
    # Create while loop to repeat till get the correct data
    while True:
        # Adjust indentation for 
        # iteration data request and validation 
        print("Please enter sales data from the last market")
        print("Data should be six numbers, seperated by commas")
        print("Example: 10,20,30,40,50,60\n")


        data_str = input("Enter your data here: ")
        
        # convert data string to list seperated by comma
        sales_data = data_str.split(",")
        
        #  Use input validation to end while loop
        if validate_data(sales_data):
            # Add a print statement to confirm valid data
            print('Data provided is valid!')
            break
    
    # Return validated sales data
    return sales_data

def validate_data(values):
    """
    Inside try, convert all string values into integers.
    Rise ValueError if string cannot be cnverted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values are expected, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e} please try again \n')
        # if the error statment araise, return False
        return False

    #  Get the funtion to call of if data provied correct
    #  Return True
    return True



def update_sales_worksheet(data):
    """"
    Update sales worksheet, add new row with the list data provided.
    """
    print('Updating sales worksheet....\n')
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('Sales datasheet updated successfully...\n')


# Call a new variable to add data
data = get_sales_data()
#  convert data provided to int
sales_data = [int(num) for num in data]
# call update datasheet funtion
update_sales_worksheet(sales_data)