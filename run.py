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

    for i, row in enumerate(budget_records[1:], start=2):  # Skip header, adjust index for update_cell
        category = row[0]
        if category in expenses_by_category:
            SHEET.worksheet('budget').update_cell(i, 3, expenses_by_category[category])
    print("Budget sheet updated successfully with actual amounts.\n")


def update_surplus_deficit():
    """
    Updates the 'Surplus/Deficit' column in the 'budget' worksheet.
    """
    budget_sheet = SHEET.worksheet('budget')
    budget_records = budget_sheet.get_all_values()[1:]  # Exclude the header row

    for i, row in enumerate(budget_records, start=2):  # start=2 to align with Google Sheets' 1-based indexing
        budgeted = float(row[1]) if row[1] else 0  # Conversion to float; Column B is "Budgeted Amount"
        actual = float(row[2]) if row[2] else 0    # Conversion to float; Column C is "Actual Amount"
        surplus_deficit = budgeted - actual        # Calculate "Budgeted Amount" - "Actual Amount"
        budget_sheet.update_cell(i, 4, surplus_deficit)  # Update the 4th column (D) with surplus/deficit

    print("Budget sheet's Surplus/Deficit column updated successfully.\n")


def main():
    print("Welcome to the Personal Finance Tracker.\n")
    while True:
        action = input("Choose action - 'add' for adding data, 'update budget' to refresh budget, 'quit' to exit: ").lower()
        if action == 'add':
            data_type = input("Type 'expense' or 'income' to specify the data type: ").lower()
            if data_type not in ['expense', 'income']:
                print("Invalid type. Please choose 'expense' or 'income'.\n")
                continue

            data = get_financial_data(data_type)
            if data:
                worksheet_name = "expenses" if data_type == 'expense' else "income"
                update_worksheet(data, worksheet_name)
                if data_type == 'expense':  # Only update budget and surplus/deficit after an expense is added
                    update_actual_amounts()  # Ensure "Actual Amount" is updated
                    update_surplus_deficit()  # Then, calculate and update "Surplus/Deficit"
                print("Data added successfully.\n")
            else:
                print("Failed to add data. Please try again.\n")
        elif action == 'update budget':  # Allows manual trigger to update the budget calculations
            update_actual_amounts()
            update_surplus_deficit()
        elif action == 'quit':
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid action. Please choose 'add', 'update budget', or 'quit'.\n")

if __name__ == "__main__":
    main()
