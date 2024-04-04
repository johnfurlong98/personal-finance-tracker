# Personal Finance Tracker

Welcome to Personal Finance Tracker, a place where you can track your income and expenses and budget for expexted expenses.

Live link to Project on Heroku : (https://personal-finance-tracker1-a9613824dabe.herokuapp.com/)

Live link to Project on Github : (https://github.com/johnfurlong98/personal-finance-tracker)

Live link to Google Sheets : (https://docs.google.com/spreadsheets/d/1hlqQIDcCy1w8jJdtelROL88UdgKCpmyeFF5UgE-qOno/edit?usp=sharing)

## Project Overview

- The Personal Finance Tracker is a command-line tool designed to help users manage their personal finances. It leverages Google Sheets as a backend API. It allows users to input their income and expenses, track their spending across different categories, and monitor their overall financial health.Users can set budgets for different expense categories and track their spending against these budgets(Currently, the application requires users to manually set a budget for anticipated expenses by directly inputting the budget category and the allocated amount into the budget sheet. When a user enters an expense via the terminal, if the expense's category matches one of the predefined categories in the budget, the application then calculates and displays the variance between the actual spent amount and the initially budgeted amount. This process necessitates that categories and budget allocations are accurately entered and matched in the budget sheet for the functionality to operate as intended.)

## Key Project Goals

- Learning Financial Management: Serve as an educational tool for individuals looking to improve their financial literacy and management skills.
- Introduction to Python and APIs: Demonstrate basic principles of Python programming and API integration for accessing and manipulating financial data.
- User Engagement: Create an intuitive and user-friendly interface that makes it easy for users to input their financial data and track their expenses.
- Extendibility: Structure the code in a way that allows for easy extension, such as features in the future.

## Target Audience

- Individuals Seeking Financial Stability: People who want to gain better control over their finances, manage their expenses, and save money for future goals.

- Young Professionals: Recent graduates and young professionals who are starting their careers and want to establish good financial habits early on.

- Families and Households: Families and households looking to budget effectively, track their spending, and plan for their financial future.

- Freelancers and Gig Workers: Freelancers, contractors, and gig workers who have irregular income streams and need to manage their finances accordingly.

- Small Business Owners: Entrepreneurs and small business owners who want to keep track of their business expenses, income, and cash flow.

- Students and College Graduates: Students and recent college graduates who are learning to manage their finances independently for the first time.

- Retirees and Seniors: Retirees and seniors who want to maintain financial stability during retirement and make the most of their savings and investments.

- Anyone Interested in Financial Management: Essentially, anyone who wants to take control of their finances, understand their spending habits, and work towards achieving their 
  financial goals.

## Future features to implement

- A key enhancement I had envisioned for the application was the ability to update the budget category and the budgeted amount directly within the app, rather than through the Google Sheet interface. Had time constraints not been a factor, I would have prioritized the development of this feature to offer a more integrated and seamless user experience.

## User Experience - UX

### User Stories

**As a user, I want to:**

- Quickly understand how to input the data .
- Easily navigate through the interface.
- Have clear feedback on the outcome .

## Conclusion

- The Personal Finance Planner is a user-friendly tool designed to empower individuals in taking control of their financial well-being. With features for expense tracking, budget management, and insightful financial analysis, it offers a comprehensive solution to help users make informed decisions, achieve financial goals, and pave the way towards a more secure future.

## Features

- Add Income and Expenses: Users can input their income and expenses, including the date, category, amount, and description.
- View Summary: Users can view a summary of their total income, total expenses, and net income.
- Budget Management: Users can set budgets for different expense categories and track their spending against these budgets.
- Financial Insights: Users can get insights into their spending habits.

## Technogolgy Used

### Languages Used
- Python 

### Programs Used
- I used Google Sheets API.
- I used Google Drive API.

## Testing

### Startup and Authentication:

- Verify the application starts without errors.
- Ensure the application can authenticate with Google Sheets using the provided credentials.

### User Interface and Prompts:

- Check if the initial instructions and options are clearly displayed to the user.
- Confirm that the application correctly prompts the user for input at each step.

### Input Validation:

- Attempt to enter invalid formats for dates, amounts, and other fields to test input validation.
- Test with missing information (e.g., only providing 3 out of 4 required pieces of data) to see if the application handles it gracefully.

### Adding Data:

- Add an income entry and verify it appears correctly in the Google Sheet.
- Add an expense entry and check its accuracy in the corresponding Google Sheet.
- Attempt to add entries with future dates, past dates, and the current date to ensure date handling is correct.

### Calculations:

- Verify that net income calculations (total income - total expenses) are correct after adding new entries.
- Add several expenses in different categories and confirm the total expenses calculation is accurate.
- Check the calculation of total income with multiple income sources.

### Sheet Updates:

- Confirm that the 'Actual Amount' column in the Budget sheet updates correctly based on new expenses.
- Verify that the 'Surplus/Deficit' column in the Budget sheet accurately reflects the difference between budgeted and actual amounts.

### Error Messages and Exception Handling:

- Test the application's response to Google Sheets API errors (e.g., by temporarily revoking access).
- Enter invalid actions or data types when prompted to check if the application provides a clear and helpful error message.

### User Experience:

- Evaluate the clarity of user prompts and messages.

## Validator Testing

- I used Python checker to make sure my code meets the standards Python PEP8. (https://www.pythonchecker.com/)

## Bugs

- Initially, the validation accepted any number of digits for year, day, and month without checking their correctness against common date formats, potentially leading to dates like "123-456-7890" being accepted. This was because the explicit checks focused on the presence of digits and certain length requirements, but not on the logical range or format of those numbers.

To solve this, we streamlined the process by using datetime.strptime(values[0], '%d-%m-%Y'), which inherently checks for the correct format and logical calendar dates, such as ensuring the month is between 1 and 12 and the day is valid for the given month. This effectively prevented the acceptance of illogical dates with incorrect numbers of digits, ensuring that only valid dates in the DD-MM-YYYY format, with proper day and month values, are accepted.

## Deployment  
- Go to the home page on "Heroku", click "new", then proced to click "create new app".
- Choose app name and region, click "create app".
- Navigate to the "settings tab", then click "reveal config vars", then in "key box" section type "CREDS" and in the "value" section copy and paste the full "creds.json file" 
  and click "add". follow the same steps to add the "PORT" for "key" and "8000" for "value".
- Then also in the "settings tab" navigate to "add buildpack" click "add buildpack" and select "Python" then add and then select "node.js" and add.
- Navigate to the "deploy" tab, click "connect to github", search for your repository by name the same as on github, then click "connect".
- Then choose "automatic deploy" or "manual deploy".
- When the app is successfully deployed click "view app". 

## Forking this project
- Fork this project by:
- Open [Github]()
- on the project to be deployed.
- Go to the "Settings".
- Go down to the "GitHub Pages".
- Click on "Check it out here!".
- Click the "main" branch and select "Save".

## Cloning This Project
- Clone this project following the steps:
- Open GitHub.
- Click on the project to be cloned.
- You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon to copy the URL.
- Once you click the button the fork will be in your repository.
- Open a new terminal.
- Change the current working directory to the location that you want the cloned directory.
- Type 'git clone' and paste the URL copied in previous steps.
- Click 'Enter' and the project is cloned.

## Content

- I reffered to code from the modules on Python to help me with this project.
