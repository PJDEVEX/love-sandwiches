# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#  import the whole library
import gspread
#  improt only creadential class
from google.oauth2.service_account import Credentials
# # import pprint 
# from pprint import pprint

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

        data_str = input("Enter your data here: \n")
        
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

# def update_sales_worksheet(data):
#     """"
#     Update sales worksheet, add new row with the list data provided.
#     """
#     print('Updating sales worksheet....\n')
#     sales_worksheet = SHEET.worksheet('sales')
#     sales_worksheet.append_row(data)
#     print('Sales datasheet updated successfully...\n')

# def update_surplus_worksheet(data):
#     """
#     Update surplus worksheet, add new row with the surplus data calculated
#     """
#     print("Updating surplus worksheet...\n")
#     surplus_worksheet = SHEET.worksheet("surplus")
#     surplus_worksheet.append_row(data)
#     print("Surplus worksheet updated successfully.\n")

# refactoring update functions
def update_worksheet(data, worksheet):
    """
    Update relevent worksheet, 
    Sales - add a new row with the sales data provided
    Surplus - add new row with the surplus data calculated
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")


def calculate_surplus_data(sales_row):
    """
    Campare sales with stock and calculate the surplus for each item

    The surplus is defined as Sales figure minus stock before the market:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold.
    """
    print('Calculating surplus data calculation...\n')
    stock = SHEET.worksheet('stock').get_all_values()
    # Access the last row of the stock worksheet
    stock_row = stock[-1]
    
    surplus_data = []
    # itarating for calculating surplus values
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales # use int to convert sting to int
        # add the calucated data to surplus list
        surplus_data.append(surplus)

    return surplus_data

def get_last_5_entries_sales():
    """
    Collect columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and return the data 
    as a list of lists
    """
    sales = SHEET.worksheet("sales")
    # column = sales.col_values(3)
    # print(column)

    columns = []
    # for ind in range(6):
    # remove index 0 from the list 
    # getting numbers from 1 to 6
    for ind in range(1, 7):
        column = sales.col_values(ind)
        # get only last 5 items
        columns.append(column[-5:])
    # pprint(columns)

    return columns

def calculate_stock_data(data):
    """
    Calculate the avarage stock for each items type, adding %
    """
    print("Calculating stock data...\n")
    new_stock_data = []
    
    for column in data:
        int_column = [int(num) for num in column]
        avarage = sum(int_column) / len(int_column)
        stock_num = avarage * 1.1
        new_stock_data.append(round(stock_num))
    
    return new_stock_data


def main():
    """
    Run all program functions
    """
    # Call a new variable to add data
    data = get_sales_data()
    #  convert data provided to int
    sales_data = [int(num) for num in data]
    # call update datasheet funtion
    update_worksheet(sales_data, "sales")
    # call claculate surplus function
    new_surplus_data = calculate_surplus_data(sales_data)
    # call update suplus worksheet function
    update_worksheet(new_surplus_data, "surplus")
    # create a sales_colunm variable for the fuction
    sales_columns = get_last_5_entries_sales()
    # call the calcualte_stock_data fuction with sales_columns argument
    stock_data = calculate_stock_data(sales_columns)
    # call update stock data function
    update_worksheet(stock_data, "stock")

print('Welcome to LOVE Sandwiches Data Automation')
main()

# 1010000000111010101010000011111111110101010101101010101001