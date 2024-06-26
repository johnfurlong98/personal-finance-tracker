import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('personal_finance_tracker')


def get_financial_data(data_type):
    """
    Prompt the user for financial data based on the specified type (expense or income).
    """
    print(f"\nPlease enter your {data_type} data in the following format:")
    print("Date (DD-MM-YYYY), Category, Amount, Description")

    data_str = input("Enter your data here: \n")

    financial_data = [data.strip() for data in data_str.split(",")]

    if validate_data(financial_data):
        return financial_data
    
    return None


def validate_data(values):
    """
    Validates the financial data to ensure correct format.
    """
    if len(values) != 4:
        print("Invalid data: Exactly 4 values are required.")
        return False
    
    day, month, year = values[0].split('-')

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        print("Invalid data: Date must be in the format DD-MM-YYYY.")
        return False
    
    if len(day) != 2 or len(month) != 2:
        print("Invalid data: Day and month must have two digits.")
        return False
    
    if len(year) != 4:
        print("Invalid data: Year must have four digits.")
        return False

    try:
        datetime.strptime(values[0], '%d-%m-%Y')
    except ValueError:
        print("Invalid data: Date must be in the format DD-MM-YYYY.")
        return False

    try:
        float(values[2])
    except ValueError:
        print("Invalid data: Amount must be a valid number.")
        return False
    
    return True


def calculate_total(sheet_name):
    """
    Calculates the total amount for either the 'income' or 'expenses' worksheet.
    """
    sheet = SHEET.worksheet(sheet_name)
    records = sheet.get_all_records()
    total_amount = sum(float(record['Amount']) for record in records)
    return total_amount


def update_worksheet(data, worksheet_name):
    """
    Updates the specified worksheet with the new data.
    """
    print(f"Updating {worksheet_name} worksheet...")
    worksheet = SHEET.worksheet(worksheet_name)
    worksheet.append_row(data)
    print(f"{worksheet_name} worksheet updated successfully.\n")

    calculate_and_display_net_income()


def calculate_and_display_net_income():
    """
    Calculates net income (total income - total expenses) and displays it in the terminal.
    """
    total_income = calculate_total('income')
    total_expenses = calculate_total('expenses')
    net_income = total_income - total_expenses
    
    print(f"Net Income: {net_income}")


def update_actual_amounts():
    """
    Updates the Actual Amount column in the Budget sheet based on expenses.
    """
    expenses_records = SHEET.worksheet('expenses').get_all_records()
    budget_records = SHEET.worksheet('budget').get_all_values()

    expenses_by_category = {}
    for record in expenses_records:
        category, amount = record['Category'], float(record['Amount'])
        if category in expenses_by_category:
            expenses_by_category[category] += amount
        else:
            expenses_by_category[category] = amount

    for i, row in enumerate(budget_records[1:], start=2):
        category = row[0]
        if category in expenses_by_category:
            SHEET.worksheet('budget').update_cell(i, 3, expenses_by_category[category])
    print("Budget sheet updated successfully with actual amounts.\n")


def update_surplus_deficit():
    """
    Updates the 'Surplus/Deficit' column in the 'budget' worksheet.
    """
    budget_sheet = SHEET.worksheet('budget')
    budget_records = budget_sheet.get_all_values()[1:]

    for i, row in enumerate(budget_records, start=2):  
        budgeted = float(row[1]) if row[1] else 0  
        actual = float(row[2]) if row[2] else 0    
        surplus_deficit = budgeted - actual        
        budget_sheet.update_cell(i, 4, surplus_deficit)  

    print("Budget sheet's Surplus/Deficit column updated successfully.\n")


def main():
    print("Welcome to the Personal Finance Tracker.\n")
    print("Please ensure you've entered your budget categories and amounts into the budget sheet before proceeding. This allows the app to accurately compare your actual expenses against your planned budget.\n")
    while True:
        action = input("Choose action - 'add' for adding data,'quit' to exit:\n").lower()
        if action == 'add':
            data_type = input("Type 'expense' or 'income' to specify the data type:\n").lower()
            if data_type not in ['expense', 'income']:
                print("Invalid type. Please choose 'expense' or 'income'.\n")
                continue

            data = get_financial_data(data_type)
            if data:
                worksheet_name = "expenses" if data_type == 'expense' else "income"
                update_worksheet(data, worksheet_name)

                if data_type == 'expense':  
                    update_actual_amounts()
                    update_surplus_deficit()  
                print("Data added successfully.\n")
            else:
                print("Failed to add data. Please try again.\n")
        elif action == 'update budget':
            update_actual_amounts()
            update_surplus_deficit()
            print("Budget sheet updated successfully.\n")
        elif action == 'quit':
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid action. Please choose 'add', 'update budget', or 'quit'.\n")

if __name__ == "__main__":
    main()
