# Personal Finance Manager

A feature-rich **command-line Personal Finance Manager built with Python** that allows users to create and manage accounts, perform financial transactions, track income and expenses, manage budgets, search and filter transaction history, generate financial reports, view account statistics, and save/load data.

This project was built to strengthen my understanding of **Python programming, data structures, validation, file handling, JSON persistence, functions, classes, and real-world project development**.

---

## Features

### Account Management

* Create personal bank accounts
* Supports **Savings** and **Current** accounts
* Stores:

  * Account holder name
  * Age
  * Phone number
  * Account type
  * Current balance
  * Transaction history
  * Budget information
* Automatically generates unique account numbers

### Money Transactions

* Deposit money
* Withdraw money
* Transfer money between accounts
* Maintains balance after every transaction
* Prevents invalid transactions through validation

### Income & Expense Management

* Add income entries
* Add expense entries
* Categorize income sources
* Categorize expenses
* Add descriptions to financial entries
* Automatically updates account balance

### Budget Management

* Set monthly budgets
* Track spending against the budget
* View budget status

### Transaction Search

Search transaction history based on:

* Transaction type
* Category / source
* Amount
* Other transaction details

### Transaction Filtering

Filter transactions using:

* Transaction type
* Category / source
* Amount range
* Balance range

### Financial Reports

Generate a detailed financial report containing:

* Income summary
* Expense summary
* Transaction summary
* Opening and closing balance
* Net income
* Savings rate
* Highest income
* Highest expense
* Overall financial status

### Account Statistics

View detailed account statistics including:

* Total transactions
* Transaction counts by type
* Total money deposited
* Total money withdrawn
* Total transfers
* Total income
* Total expenses
* Net income
* Total money in/out
* Savings rate
* Highest income/expense
* Most frequent transaction
* Account activity
* Financial status

### Data Persistence

* Save account information to a JSON file
* Save transaction history
* Restore previously saved account data
* Displays save/load status
* Protects current data during the loading process

### Input Validation

The project includes validation for:

* Account holder names
* Age
* Phone numbers
* Account type
* Account balance
* Transaction amounts
* Menu choices
* Account numbers
* Transaction filters

Invalid inputs are handled without crashing the program.

---

## Technologies Used

* **Python 3**
* **JSON**
* Python dictionaries
* Python lists
* Functions
* Classes
* Exception handling
* File handling

---

## Main Menu

The application currently provides the following options:

```text
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Check Balance
6. Transaction History
7. Add Income
8. Add Expense
9. Set Monthly Budget
10. Budget Status
11. Search Transactions
12. Filter Transactions
13. Financial Report
14. Account Statistics
15. Save Data
16. Load Data
17. Exit
```

---

## Data Storage

Account information and transaction history are stored locally using:

```text
account.json
```

The application uses JSON serialization to save and restore account data.

---

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd Personal-Finance-Manager
```

### 3. Run the Python program

```bash
python main.py
```

> Replace `main.py` with the actual Python file name if your project uses a different filename.

---

## Concepts Practiced

This project helped me practice and apply:

* Variables and data types
* Conditional statements
* Loops
* Functions
* Lists
* Dictionaries
* Nested data structures
* Classes and objects
* Exception handling
* Input validation
* File handling
* JSON serialization/deserialization
* Searching and filtering
* Data aggregation
* Financial calculations
* Modular program design
* CLI application design

---

## Project Structure

```text
Personal-Finance-Manager/
│
├── main.py
├── account.json
└── README.md
```

> The exact file structure may vary depending on the current project organization.

---

## Future Improvements

Possible improvements for future versions include:

* Add transaction dates and timestamps
* Generate true monthly/yearly reports
* Support multiple historical financial periods
* Improve account-specific opening balance tracking
* Add graphical financial charts
* Add CSV export
* Add password/PIN-based account security
* Improve data encryption and security
* Add recurring income and expense tracking
* Add more advanced financial analytics
* Build a GUI version
* Eventually create a web-based version

---

## About the Project

This project was developed as a **hands-on Python project** to move beyond small practice programs and build a larger real-world application.

The main focus was not just making the program work, but also implementing:

* Proper input validation
* Edge-case handling
* Structured functions
* Consistent user interface
* Meaningful financial calculations
* Persistent data storage
* A scalable project structure

---

## License

This project is currently intended for **educational and personal use**.
