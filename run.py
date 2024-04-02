import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('personal _finance_tracker')

expenses = SHEET.worksheet('expenses')

data = expenses.get_all_values()


def get_financial_data(data_type):
    """
    Prompt the user for financial data based on the specified type (expense or income).
    """
    print(f"\nPlease enter your {data_type} data in the following format:")
    print("Date (DD-MM-YYYY), Category, Amount, Description")
    data_str = input("Enter your data here: ")
    financial_data = [data.strip() for data in data_str.split(",")]

    if validate_data(financial_data):
        return financial_data
    else:
        return None


def validate_data(values):
    """
    Validates the financial data to ensure correct format.
    """
    if len(values) != 4:
        print("Invalid data: Exactly 4 values are required.")
        return False
    try:
        float(values[2])
    except ValueError:
        print("Invalid data: Amount must be a valid number.")
        return False
    return True


def update_worksheet(data, worksheet_name):
    """
    Updates the specified worksheet with the new data.
    """
    print(f"Updating {worksheet_name} worksheet...")
    worksheet = SHEET.worksheet(worksheet_name)
    worksheet.append_row(data)
    print(f"{worksheet_name} worksheet updated successfully.\n")



def main():
    # Testing the get_financial_data function
    print("Testing get_financial_data function")
    test_data = get_financial_data('expense')  # Test with 'expense' or 'income'
    print(f"Returned data: {test_data}")

if __name__ == "__main__":
    main()
