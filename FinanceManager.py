storedAccounts = 0
storedTransactions = 0

def validateCommand(action):

    if not action:
        return None , '---> Please select an Option first..'

    if not action.isnumeric():
        return None , '---> Invalid Option selected..'

    command = int(action)

    if not 1 <= command <= 17:
        return None , '---> Option must be selected within 1 to 17'

    return command , None

def validateHolderName(name):

    if not name:
        return None , '---> First enter the holder name.'

    if not name.replace(" ", "").isalpha():
        return None , '---> Invalid Holder name entered'

    name = name.title()

    return name , None

def validateAccountType(accType):

    if not accType:
        return None, '---> Select an Account type first'

    accType = accType.title()

    if accType not in ('Saving', 'Savings', 'Current'):
        return None, '---> Account type must be either Savings or Current'

    if accType == 'Saving':
        accType = 'Savings'

    return accType, None

def validateBalance(balance):

    if not balance:
        return None , '---> Enter the Initial Balance before proceeding'

    try:
        balance = float(balance)

    except ValueError:
        return None , '---> Initial Balance must be a valid number'

    if balance <= 0:
        return None , '---> Amount must be greater than Zero'

    return balance  , None

def validateAmount(amount):

    if not amount:
        return None , '---> Enter the Amount before proceeding'

    try:
        amount = float(amount)

    except ValueError:
        return None , '---> Amount must be a valid number'

    if amount <= 0:
        return None , '---> Amount must be greater than Zero'

    return amount  , None

def validateAge(age):

    if not age:
        return None , '---> Enter the holder age first'

    if not age.isnumeric():
        return None , '---> Invalid age of the holder entered'

    age = int(age)

    if not 18 <= age <= 80:
        return None , '---> Age of the holder must be within 18 to 80 years'

    return age , None

def validatePhoneNumber(number):

    if not number: 
        return None , '---> Phone number must be entered'

    if not number.isnumeric():
        return None , '---> Invalid phone number entered'

    if len(number) != 10:
        return None , '---> Phone number must be of 10 digits'

    return number , None

def validateChoice(choice , startValue , endingValue):

    if not choice:
        return None , '---> Select a option before proceeding.'

    if not choice.isnumeric():
        return None , '---> Invalid choice entered.'

    choice = int(choice)

    if not startValue <= choice <= endingValue:
        return None , f'---> Selection must be within options {startValue} to {endingValue}.'

    return choice , None

def generateAccNumber(letter_count=5, digit_count=5):

    import random
    import string

    letters = ''.join(random.choices(string.ascii_letters, k=letter_count)).title()
        
    digits = ''.join(random.choices(string.digits, k=digit_count))
        
    return letters[:3] + digits[:3] + letters[3:5] + digits[3:]

def displaySearchResult(count , credentials):

    print(f'''

[{count + 1}] {credentials['type']}
    Category       : {credentials['category'] if credentials['type'] in ('Income' , 'Expense') else '----'}
    Amount         : ₹{credentials['amount']:.2f}
    Description    : {credentials['description'] if credentials['type'] in ('Income' , 'Expense') else '----'}
    Balance After  : ₹{credentials['balanceAfter']:.2f}
                ''')

    if credentials['type'] == 'Transfer Out':

        print(f'''
    To             : {credentials['to']}
        ''')

    elif credentials['type'] == 'Transfer In':

            print(f'''
    From           : {credentials['from']}
        ''')

def displayFilterResult(count , credentials):

    print(f'''
[{count + 1}] {credentials['type']}
    Category       : {credentials['category'] if credentials['type'] in ('Income' , 'Expense') else '----'}
    Amount         : ₹{credentials['amount']:.2f}
    Description    : {credentials['description'] if credentials['type'] in ('Income' , 'Expense') else '----'}
    Balance After  : ₹{credentials['balanceAfter']:.2f}

    To             : {credentials['to'] if credentials['type'] == 'Transfer Out' else '----'}
    From           : {credentials['from'] if credentials['type'] == 'Transfer In' else '----'}
    ''')

def displayIncomeReport(transactions):

    totalIncome = 0
    incomeSources = []

    for transaction in transactions:

        if transaction['type'] == 'Income':
            totalIncome += transaction['amount']
            incomeSources.append([transaction['category'] , transaction['amount']])

    print(f'''
                INCOME SUMMARY

------------------------------------------------

        Total Income     : ₹{totalIncome:.2f}

Income Sources :
    ''')

    if not incomeSources:
        print('''
No income transactions recorded yet.
        ''')

    else:
        for idx in range(len(incomeSources)):

            sourceInfo = incomeSources[idx]

            print(f'''
{idx + 1}. {sourceInfo[0]}            ₹{sourceInfo[1]:.2f}
            ''')

    print('''
================================================
    ''')

def displayExpenseReport(transactions):

    totalExpense = 0   
    expenseSources = []

    for transaction in transactions:

        if transaction['type'] == 'Expense':
            totalExpense += transaction['amount']
            expenseSources.append([transaction['category'] , transaction['amount']])

    print(f'''
                EXPENSE SUMMARY

------------------------------------------------

        Total Expense     : ₹{totalExpense:.2f}
    
Expense Categories :
        ''')
    
    if not expenseSources:
            print('''
No Expense transactions recorded yet.
            ''')
    
    else:

        for idx in range(len(expenseSources)):
    
            sourceInfo = expenseSources[idx]
    
            print(f'''
{idx + 1}. {sourceInfo[0]}           ₹{sourceInfo[1]:.2f}
            ''')
    
    print('''
================================================
        ''')

def getAllTransactions(transactions):

    allTransactions = {}
    totalTransactions = 0

    for transaction in transactions:

        transactionType = transaction['type'].title()

        if transactionType in allTransactions:

            allTransactions[transactionType] += 1

        else:

            allTransactions[transactionType] = 1
        totalTransactions += 1

    return totalTransactions , allTransactions

def getAllTransactionsAmount(transactions):

    allTransactionsAmount = {}

    for transaction in transactions:

        transactionType = transaction['type']

        if transactionType in allTransactionsAmount:

            allTransactionsAmount[transactionType] += transaction['amount']

        else:

            allTransactionsAmount[transactionType] = transaction['amount']

    return allTransactionsAmount

def getHighest(transactions):

    highestIncome = 0
    highestExpense = 0

    for transaction in transactions:

        transactionType = transaction['type']

        if transactionType == 'Income' and transaction['amount'] > highestIncome:
            highestIncome = transaction['amount']
        elif transactionType == 'Expense' and transaction['amount'] > highestExpense:
            highestExpense = transaction['amount']

    return highestIncome , highestExpense

def getSavingRateAndStatus(netIncome , allTransactionsAmount):

    if allTransactionsAmount.get('Income' , 0) == 0:

        savingsRate = 'N/A'

    else:

        savingsRate = round((netIncome / allTransactionsAmount['Income']) * 100 , 2)
        savingsRate = str(savingsRate) + '%'

    if netIncome > 0:
        status = 'PROFITABLE'
    elif netIncome == 0:
        status = 'BREAK-EVEN'
    else:
        status = 'LOSS'

    return savingsRate , status

def displayTransactionsSummary(openingBalance , currentBalance , transactions):

    totalTransactions , allTransactionsDict = getAllTransactions(transactions)

    allTransactionsAmount = getAllTransactionsAmount(transactions)

    highestIncome , highestExpense = getHighest(transactions)

    netIncome = allTransactionsAmount.get('Income' , 0) - allTransactionsAmount.get('Expense' , 0)

    savingsRate , status = getSavingRateAndStatus(netIncome , allTransactionsAmount)

    print(f'''
              TRANSACTION SUMMARY

------------------------------------------------

Total Transactions : {totalTransactions}

Deposits           : {allTransactionsDict.get('Deposit' , 0)}
Withdrawals        : {allTransactionsDict.get('Withdrawal' , 0)}
Transfers In       : {allTransactionsDict.get('Transfer In' , 0)}
Transfers Out      : {allTransactionsDict.get('Transfer Out' , 0)}
Income Entries     : {allTransactionsDict.get('Income' , 0)}
Expense Entries    : {allTransactionsDict.get('Expense' , 0)}

------------------------------------------------

Opening Balance    : ₹{openingBalance:.2f}
Total Income       : ₹{allTransactionsAmount.get('Income' , 0):.2f}
Total Deposits     : ₹{allTransactionsAmount.get('Deposit' , 0):.2f}
Total Transfers In : ₹{allTransactionsAmount.get('Transfer In' , 0):.2f}

Total Expenses     : ₹{allTransactionsAmount.get('Expense' , 0):.2f}
Total Withdrawals  : ₹{allTransactionsAmount.get('Withdrawal' , 0):.2f}
Total Transfers Out: ₹{allTransactionsAmount.get('Transfer Out' , 0):.2f}

Closing Balance    : ₹{currentBalance:.2f}

================================================

              FINANCIAL OVERVIEW

------------------------------------------------

Net Income         : ₹{netIncome:.2f}
Savings Rate       : {savingsRate}

Highest Income     : ₹{highestIncome:.2f}
Highest Expense    : ₹{highestExpense:.2f}

------------------------------------------------

Report Status      : {status}

================================================
    ''')

def netMoneyInAndOut(transactions):

    totalMoneyIn = 0
    totalMoneyOut = 0

    for transaction in transactions:

        if transaction['type'] in {'Income' , 'Deposit' , 'Transfer In'}:
            totalMoneyIn += transaction['amount']
        else:
            totalMoneyOut += transaction['amount']

    return totalMoneyIn , totalMoneyOut

def mostFrequentTransactions(allTransactions):

    frequentTransaction = None
    transactionCount = 0

    for transaction in allTransactions:
        if allTransactions[transaction] > transactionCount:
            transactionCount = allTransactions[transaction]
            frequentTransaction = transaction

    return frequentTransaction


def displayStatistics(accNumber , credentials):

    transactions = credentials['transactions']

    totalTransactions , allTransactionsDict = getAllTransactions(transactions)

    allTransactionsAmount = getAllTransactionsAmount(transactions)

    netIncome = allTransactionsAmount.get('Income' , 0) - allTransactionsAmount.get('Expense' , 0)

    totalMoneyIn , totalMoneyOut = netMoneyInAndOut(transactions)

    savingsRate , status = getSavingRateAndStatus(netIncome , allTransactionsAmount)

    highestIncome , highestExpense = getHighest(transactions)

    firstTransaction = transactions[0]
    lastTransaction = transactions[-1]

    frequentTransaction = mostFrequentTransactions(allTransactionsDict)

    print(f'''
                 ACCOUNT OVERVIEW

------------------------------------------------

Account Holder    : {credentials['name']}
Account Number    : {accNumber}
Account Type      : {credentials['accountType']}

Current Balance   : ₹{credentials['balance']}

------------------------------------------------

              TRANSACTION STATISTICS

------------------------------------------------

Total Transactions : {totalTransactions}

Deposits            : {allTransactionsDict.get('Deposit' , 0)}
Withdrawals         : {allTransactionsDict.get('Withdrawal' , 0)}
Transfers In        : {allTransactionsDict.get('Transfer In' , 0)}
Transfers Out       : {allTransactionsDict.get('Transfer Out' , 0)}
Income Entries      : {allTransactionsDict.get('Income' , 0)}
Expense Entries     : {allTransactionsDict.get('Expense' , 0)}

------------------------------------------------

              TRANSACTION AMOUNTS

------------------------------------------------

Total Deposited     : ₹{allTransactionsAmount.get('Deposit' , 0):.2f}
Total Withdrawn     : ₹{allTransactionsAmount.get('Withdrawal' , 0):.2f}

Total Transfers In  : ₹{allTransactionsAmount.get('Transfer In' , 0):.2f}
Total Transfers Out : ₹{allTransactionsAmount.get('Transfer Out' , 0):.2f}

Total Income        : ₹{allTransactionsAmount.get('Income' , 0):.2f}
Total Expenses      : ₹{allTransactionsAmount.get('Expense' , 0):.2f}

------------------------------------------------

              FINANCIAL STATISTICS

------------------------------------------------

Net Income          : ₹{netIncome:.2f}

Total Money In      : ₹{totalMoneyIn:.2f}
Total Money Out     : ₹{totalMoneyOut:.2f}

Savings Rate        : {savingsRate}

Highest Income      : ₹{highestIncome:.2f}
Highest Expense     : ₹{highestExpense:.2f}

------------------------------------------------

             ACCOUNT ACTIVITY

------------------------------------------------

First Transaction   : {firstTransaction['type']}
Last Transaction    : {lastTransaction['type']}

Total Transaction Types : {len(allTransactionsDict)}

Most Frequent Transaction : {frequentTransaction}

------------------------------------------------

             ACCOUNT STATUS

------------------------------------------------

Current Balance     : ₹{credentials['balance']}

Financial Status    : {status}
Activity Status     : ACTIVE

================================================
    ''')

def displayCancellation():

    print('''
================ SAVE DATA ========================

------------------------------------------------

                DATA BACKUP

------------------------------------------------

Data saving cancelled by the holder.

No changes were made to the saved data.

------------------------------------------------

Save Status : CANCELLED

================================================
    ''')

def displaySuccess(totalAccount , totalTransactions):

    storedAccounts = totalAccount
    storedTransactions = totalTransactions

    print(f'''
================ SAVE DATA ========================

------------------------------------------------

                DATA BACKUP

------------------------------------------------

Accounts Saved       : {totalAccount}
Transactions Saved   : {totalTransactions}

------------------------------------------------

Data saved successfully.

Your account information and transaction
history have been securely stored.

------------------------------------------------

Save Status : SUCCESS

================================================
    ''')

def displayError():

    print('''
================ SAVE DATA ========================

------------------------------------------------

                DATA BACKUP

------------------------------------------------

Unable to save account data.

An error occurred while saving the data.

------------------------------------------------

Save Status : FAILED

================================================
    ''')

def saveToDatabase(accounts):

    import json as js
    import copy

    copyData = copy.deepcopy(accounts)

    try:

        with open("account.json", "w") as jsonFile:
        
            js.dump(copyData, jsonFile, indent=4)

            totalAccount = len(accounts)
            totalTransaction = 0

            for acc in accounts:
                totalTransaction += len(accounts[acc]['transactions'])

            displaySuccess(totalAccount , totalTransaction)

    except FileNotFoundError:

        displayError()

def displayLoadCancellation():

    print('''
================ LOAD DATA ========================

------------------------------------------------

                RESTORE DATA

------------------------------------------------

Data loading cancelled by the holder.

Current account data remains unchanged.

------------------------------------------------

Load Status : CANCELLED

================================================
    ''')

def displayLoadSuccess():

    print(f'''
================ LOAD DATA ========================

------------------------------------------------

                RESTORE DATA

------------------------------------------------

Accounts Loaded       : {storedAccounts}
Transactions Loaded   : {storedTransactions}

------------------------------------------------

Data loaded successfully.

All saved account information and transaction
history have been restored.

------------------------------------------------

Load Status : SUCCESS

================================================
    ''')

def noSaveDataFound():

    print('''
================ LOAD DATA ========================

------------------------------------------------

                RESTORE DATA

------------------------------------------------

No saved account data was found.

Please save your account data before
attempting to load it.

------------------------------------------------

Load Status : NO DATA FOUND

================================================
    ''')

def displayLoadError():

    print('''
================ LOAD DATA ========================

------------------------------------------------

                RESTORE DATA

------------------------------------------------

Unable to load saved account data.

The saved data could not be read correctly.

------------------------------------------------

Load Status : FAILED

================================================
    ''')

def loadFromFile(accounts):

    import json as js

    try: 

        with open('account.json' , "r") as jsonFile:

            try:

                accounts = js.load(jsonFile)

            except js.JSONDecodeError:

                noSaveDataFound()
                return None , 'error'

            displayLoadSuccess()
            return accounts , None

    except FileNotFoundError:

        displayLoadError()
        return None , 'error'

class FinanceManager:

    def __init__(self):

        self.command = None
        self.accounts = {}
        self.openingBalance = 0

    def run(self):

        while self.command != 17:

            self.displayMenu()

            if self.command == 1:
                self.createAccount()

            elif self.command == 2:
                self.depositMoney()

            elif self.command == 3:
                self.withdrawMoney()

            elif self.command == 4:
                self.transferMoney()

            elif self.command == 5:
                self.checkBalance()

            elif self.command == 6:
                self.transactionHistory()

            elif self.command == 7:
                self.addIncome()

            elif self.command == 8:
                self.addExpense()

            elif self.command == 9:
                self.addBudget()

            elif self.command == 10:
                self.displayBudget()

            elif self.command == 11:
                self.searchTransactions()

            elif self.command == 12:
                self.filterTransactions()

            elif self.command == 13:
                self.financialReport()

            elif self.command == 14:
                self.accountStatistics()

            elif self.command == 15:
                self.displaySaveUI()

            elif self.command == 16:
                self.displayLoadUI()

            elif self.command == 17:

                self.terminate()

    def validateAccNumber(self , accNumber):

        if not accNumber:
            return None , '---> Enter the Account number first'

        if accNumber not in self.accounts:
            return None , '---> Account not found'

        return accNumber , None

    def displayMenu(self):

        print('''
================ PERSONAL FINANCE MANAGER ================

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
        ''')

        command = input('Enter the option here : ').strip()

        command , error = validateCommand(command)

        if error:
            print(error)
            return None

        self.command = command
        return self.command

    def createAccount(self):

        print('''
================ CREATE ACCOUNT ================
        ''')

        name = input('Enter account holder name : ').strip()

        holderName , error = validateHolderName(name)

        if error:
            print(error)
            return None

        acc = input('Enter account type (Savings/Current) : ').strip()

        accType , error = validateAccountType(acc)

        if error:
            print(error)
            return None

        balance = input('Enter initial balance : ').strip()

        initialBalance , error = validateBalance(balance)

        if error:
            print(error)
            return None

        age = input('Enter the Holders Age : ').strip()

        holderAge , error = validateAge(age)

        if error:
            print(error)
            return None

        number = input('Enter the Holders Phone number : ').strip()

        phoneNumber , error = validatePhoneNumber(number)

        if error:
            print(error)
            return None

        accountNumber = generateAccNumber()

        while accountNumber in self.accounts:
            accountNumber = generateAccNumber()

        self.openingBalance = initialBalance

        accountData = {
            'name' : holderName,
            'age' : holderAge,
            'phone' : phoneNumber,
            'balance' : initialBalance,
            'accountType' : accType,
            'transactions' : [],
            'budget' : {}
        }

        self.accounts[accountNumber] = accountData

        print(f'''
Account created successfully!

Account Number : {accountNumber}
Account Holder : {holderName}
Account Holder Age : {holderAge}
Account Type   : {accType}
Balance        : ₹{initialBalance:.2f}
Phone Number : +91 {phoneNumber}
        ''')

    def depositMoney(self):

        print('''
================ DEPOSIT MONEY ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        accNumber , error = self.validateAccNumber(inputAccNumber)

        if error:
            print(error)
            return

        holderAccount = self.accounts[accNumber]
        currentBalance = holderAccount['balance']

        print(f'''
Account Holder : {holderAccount['name']}
Current Balance : {currentBalance:.2f}

        ''')

        money = input('Enter Amount to Deposit : ₹').strip()

        moneyToDeposit , error= validateAmount(money)

        if error:
            print(error)
            return

        confirmation = input('Confirm Deposit? (Y/N) : ').strip().upper()

        print('''
------------------------------------------------
        ''')

        if confirmation not in {'Y' , 'N' , 'YES' , 'NO'}:
            print('---> Invalid Response.')
            return

        if confirmation in {'N' , 'NO'}:
            print('---> Deposition stopped by the Holder.')
            return

        holderAccount['balance'] = currentBalance + moneyToDeposit

        print(f'''
Deposit successful!

Amount Deposited : ₹{moneyToDeposit}
Previous Balance : ₹{currentBalance}
New Balance      : ₹{holderAccount['balance']:.2f}
------------------------------------------------
        ''')

        userTransaction = {
            'type' : 'Deposit',
            'amount' : moneyToDeposit,
            'balanceAfter' : holderAccount['balance']
        }

        holderAccount['transactions'].append(userTransaction)

    def withdrawMoney(self):

        print('''
================ WITHDRAW MONEY ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        accNumber , error = self.validateAccNumber(inputAccNumber)

        if error:
            print(error)
            return

        holderAccount = self.accounts[accNumber]
        currentBalance = holderAccount['balance']

        print(f'''
Account Holder  : {holderAccount['name']}
Current Balance : ₹{currentBalance:.2f}
        ''')

        money = input('Enter Amount to Withdraw : ₹').strip()

        moneyToWithdraw , error = validateAmount(money)

        if error:
            print(error)
            return

        if moneyToWithdraw > currentBalance:
            print(f'---> Insufficient Balance\n---> Maximum amount you can withdraw: ₹{currentBalance}')
            return

        confirmation = input('Confirm Withdrawal? (Y/N) : ').strip().upper()

        print('''
------------------------------------------------
        ''')

        if confirmation not in {'Y' , 'N' , 'YES' , 'NO'}:
            print('---> Invalid Response.')
            return

        if confirmation in {'N' , 'NO'}:
            print('---> Withdrawal stopped by the Holder.')
            return

        holderAccount['balance'] = currentBalance - moneyToWithdraw

        print(f'''
Withdrawal successful!

Amount Withdrawn : ₹{moneyToWithdraw}
Previous Balance : ₹{currentBalance}
New Balance      : ₹{holderAccount['balance']:.2f}
------------------------------------------------
        ''')

        userTransaction = {
            'type' : 'Withdrawal',
            'amount' : moneyToWithdraw,
            'balanceAfter' : holderAccount['balance']
        }

        holderAccount['transactions'].append(userTransaction)       

    def transferMoney(self):

        print('''
================ TRANSFER MONEY ================
        ''')

        senderAccNumber = input('Enter Sender Account Number   : ').strip()

        if not senderAccNumber:
            print('---> Enter the Sender Account number first')
            return

        if senderAccNumber not in self.accounts:
            print('---> Sender Account not found.')
            return

        receiverAccNumber = input('Enter Receiver Account Number : ').strip()

        if not receiverAccNumber:
            print('---> Enter the Receiver Account number first')
            return

        if receiverAccNumber not in self.accounts:
            print('---> Receiver Account not found.')
            return

        if senderAccNumber == receiverAccNumber:
            print('---> Sender and Receiver accounts cannot be the same.')
            return

        senderAccount = self.accounts[senderAccNumber]
        receiverAccount = self.accounts[receiverAccNumber]

        print(f'''
------------------------------------------------

Sender Account Holder   : {senderAccount['name']}
Sender Current Balance  : ₹{senderAccount['balance']:.2f}

Receiver Account Holder : {receiverAccount['name']}
Receiver Current Balance: ₹{receiverAccount['balance']:.2f}

------------------------------------------------
        ''')

        money = input('Enter Amount to Transfer : ').strip()

        moneyToTransfer , error = validateAmount(money)

        if error:
            print(error)
            return

        if moneyToTransfer > senderAccount['balance']:
            print(f"---> Insufficient Balance in Sender's Account\n---> Maximum amount you can transfer: ₹{senderAccount['balance']}")
            return

        confirmation = input('Confirm Transfer? (Y/N) : ').strip().upper()

        print('''
------------------------------------------------
        ''')

        if confirmation not in {'Y' , 'N' , 'YES' , 'NO'}:
            print('---> Invalid Response.')
            return

        if confirmation in {'N' , 'NO'}:
            print('---> Transfer stopped by the Holder.')
            return

        senderCurrentBalance = senderAccount['balance']
        receiverCurrentBalance = receiverAccount['balance']
        senderAccount['balance'] -= moneyToTransfer
        receiverAccount['balance'] += moneyToTransfer

        print(f'''
Transfer successful!

Transfer Amount : ₹{moneyToTransfer:.2f}

Sender
Previous Balance : ₹{senderCurrentBalance:.2f}
New Balance      : ₹{senderAccount['balance']:.2f}

Receiver
Previous Balance : ₹{receiverCurrentBalance:.2f}
New Balance      : ₹{receiverAccount['balance']:.2f}

------------------------------------------------
        ''')

        senderTransaction = {
            'type' : 'Transfer Out',
            'amount' : moneyToTransfer,
            'balanceAfter' : senderAccount['balance'],
            'to' : receiverAccNumber
        }

        senderAccount['transactions'].append(senderTransaction)

        receiverTransaction = {
            'type' : 'Transfer In',
            'amount' : moneyToTransfer,
            'balanceAfter' : receiverAccount['balance'],
            'from' : senderAccNumber
        }

        receiverAccount['transactions'].append(receiverTransaction)

    def checkBalance(self):

        print('''
================ CHECK BALANCE ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        accNumber , error = self.validateAccNumber(inputAccNumber)

        if error:
            print(error)
            return

        holderAccount = self.accounts[accNumber]

        print(f'''
------------------------------------------------

Account Holder : {holderAccount['name']}
Account Number : {accNumber}
Account Type   : {holderAccount['accountType']}

Current Balance : ₹{holderAccount['balance']:.2f}

------------------------------------------------
        ''')
        

    def transactionHistory(self):

        print('''
================ TRANSACTION HISTORY ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        accNumber , error = self.validateAccNumber(inputAccNumber)

        if error:
            print(error)
            return

        holderAccount = self.accounts[accNumber]

        print(f'''
------------------------------------------------

Account Holder : {holderAccount['name']}
Account Number : {accNumber}
Current Balance : ₹{holderAccount['balance']:.2f}

------------------------------------------------

Transaction History:
        ''')

        if not holderAccount['transactions']:
            print('''
---> No transactions found.
            ''')

        else:
            for count in range(len(holderAccount['transactions'])):

                holderTransaction = holderAccount['transactions'][count]

                print(f'''
[{count + 1}] {holderTransaction['type']}
    Amount       : ₹{holderTransaction['amount']:.2f}
    Balance After: ₹{holderTransaction['balanceAfter']:.2f}
                ''')

                if 'to' in holderTransaction:

                    print(f'''
    To           : {holderTransaction['to']}
                    ''')

                elif 'from' in holderTransaction:

                    print(f'''
    From         : {holderTransaction['from']}
                    ''')

        print('''
------------------------------------------------
        ''')                  

    def addIncome(self):

        print('''
================ ADD INCOME ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        accNumber , error = self.validateAccNumber(inputAccNumber)

        if error:
            print(error)
            return

        holderAccount = self.accounts[accNumber]

        print(f'''
------------------------------------------------

Account Holder  : {holderAccount['name']}
Current Balance : ₹{holderAccount['balance']:.2f}

------------------------------------------------
        ''')

        amount = input('Enter Income Amount : ₹').strip()

        incomeAmount , error = validateAmount(amount)

        if error:
            print(error)
            return

        source = input('Enter Income Source : ').strip().title()

        if not source:
            print('---> Income source must be entered.')
            return

        if not source.replace(" " , "").isalpha():
            print('---> Invalid source entered');
            return

        description = input('Enter description : ').strip().title()

        if not description:
            print('---> Description must be entered before proceeding.')
            return

        confirmation = input('Confirm Income Entry? (Y/N) : ').strip().upper()

        print('''
------------------------------------------------
        ''')
        
        if confirmation not in {'Y' , 'N' , 'YES' , 'NO'}:
            print('---> Invalid Response.')
            return

        if confirmation in {'N' , 'NO'}:
            print('---> Income entry stopped by the Holder.')
            return

        previousBalance = holderAccount['balance']
        holderAccount['balance'] += incomeAmount

        print(f'''
Income added successfully!

Income Source  : {source}
Income Amount  : ₹{incomeAmount:.2f}
Description    : {description}

Previous Balance : ₹{previousBalance:.2f}
New Balance      : ₹{holderAccount['balance']:.2f}

------------------------------------------------
        ''')

        # Update the transaction record
        holderAccount['transactions'].append({
            'type' : 'Income',
            'category' : source,
            'amount' : incomeAmount,
            'balanceAfter' : holderAccount['balance'],
            'description' : description
        })

    def addExpense(self):

        print('''
================ ADD EXPENSE ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        accNumber , error = self.validateAccNumber(inputAccNumber)

        if error:
            print(error)
            return

        holderAccount = self.accounts[accNumber]

        print(f'''
------------------------------------------------

Account Holder  : {holderAccount['name']}
Current Balance : ₹{holderAccount['balance']:.2f}

------------------------------------------------
        ''')

        category = input('Enter expense category : ').strip().title()

        if not category:
            print('---> Expense category must be filled.')
            return

        amount = input('Enter expense amount : ').strip()

        expenseAmount , error = validateAmount(amount)

        if error:
            print(error)
            return

        if expenseAmount > holderAccount['balance']:
            print(f'---> Insufficient Balance.\n---> Maximum expense you can record: ₹{holderAccount['balance']:.2f}')
            return

        description = input('Enter description : ').strip().title()

        if not description:
            print('---> Description must be entered before proceeding.')
            return

        confirmation = input('Confirm Expense Entry? (Y/N) : ').strip().upper()

        print('''
------------------------------------------------
        ''')
        
        if confirmation not in {'Y' , 'N' , 'YES' , 'NO'}:
            print('---> Invalid Response.')
            return

        if confirmation in {'N' , 'NO'}:
            print('---> Expense entry stopped by the Holder.')
            return

        holderPreviousBalance = holderAccount['balance']
        holderAccount['balance'] -= expenseAmount

        print(f'''
Expense added successfully!

Account Number : {accNumber}
Category       : {category}
Amount         : ₹{expenseAmount:.2f}
Description    : {description}

Previous Balance : ₹{holderPreviousBalance:.2f}
New Balance      : ₹{holderAccount['balance']:.2f}

==============================================
        ''')

        holderAccount['transactions'].append({
            'type' : 'Expense',
            'category' : category,
            'amount' : expenseAmount,
            'balanceAfter' : holderAccount['balance'],
            'description' : description
        })

    def addBudget(self):

        print('''
================ SET MONTHLY BUDGET ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        accNumber , error = self.validateAccNumber(inputAccNumber)

        if error:
            print(error)
            return

        holderAccount = self.accounts[accNumber]

        print(f'''
------------------------------------------------

Account Holder   : {holderAccount['name']}
Current Balance  : ₹{holderAccount['balance']:.2f}
Current Budget   : {f'₹{holderAccount['budget']['amount']:.2f}' if holderAccount['budget'] else '----'}

------------------------------------------------
        ''')

        amount = input('Enter Budget Amount : ').strip()

        budgetAmount , error = validateAmount(amount)

        if error:
            print(error)
            return

        confirmation = input('Confirm Budget Setting? (Y/N) : ').strip().upper()

        print('''
------------------------------------------------
        ''')
        
        if confirmation not in {'Y' , 'N' , 'YES' , 'NO'}:
            print('---> Invalid Response.')
            return

        if confirmation in {'N' , 'NO'}:
            print('---> Budget entry stopped by the Holder.')
            return

        previousBudget = holderAccount['budget']['amount'] if holderAccount['budget'] else 0

        holderAccount['budget'].update({
            'amount' : budgetAmount
        })

        print(f'''
Monthly Budget updated successfully!

Previous Budget : ₹{previousBudget:.2f}
New Budget      : ₹{budgetAmount:.2f}

================================================
        ''')

    def displayBudget(self):

        print('''
================ BUDGET STATUS ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        accNumber , error = self.validateAccNumber(inputAccNumber)

        if error:
            print(error)
            return

        holderAccount = self.accounts[accNumber]

        print(f'''
------------------------------------------------

Account Holder   : {holderAccount['name']}
Account Number   : {accNumber}
        ''')

        if not holderAccount['budget']:
            print('''
---> No monthly budget has been set.

Please use Option 9 to set a monthly budget.

================================================
            ''')
            return

        expenditure = 0
        budgetAmount = holderAccount['budget']['amount']

        for transaction in holderAccount['transactions']:

            if transaction['type'] == 'Expense':
                expenditure += transaction['amount']
        remainingBudget = budgetAmount - expenditure

        budgetUsed = round((expenditure / budgetAmount) * 100 , 2)

        print(f'''
Monthly Budget   : ₹{budgetAmount:.2f}
Amount Spent     : ₹{expenditure:.2f}
{f'Remaining Budget : ₹{remainingBudget:.2f}' if expenditure <= budgetAmount else f'Budget Exceeded  : ₹{abs(remainingBudget):.2f}'}

{f'Budget Used      : {budgetUsed}%\nBudget Remaining : {100 - budgetUsed}%' if budgetUsed <= 100 else f'Budget Used      : {budgetUsed}%'}

------------------------------------------------

Status : {'Within Budget' if budgetUsed <= 100 else '⚠️ Budget Exceeded'}
================================================
        ''')

    def searchTransactions(self):

        print('''
================ SEARCH TRANSACTIONS ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        accNumber , error = self.validateAccNumber(inputAccNumber)

        if error:
            print(error)
            return

        holderAccount = self.accounts[accNumber]

        print(f'''
Account Holder : {holderAccount['name']}
Current Balance: ₹{holderAccount['balance']:.2f}

------------------------------------------------

Search By:

1. Transaction Type
2. Category / Source
3. Description
4. Amount
5. Transfer Account Number

6. Back

------------------------------------------------
        ''')

        inputChoice = input('Enter your choice : ').strip()

        choice , error = validateChoice(inputChoice , 1 , 6)

        if error:
            print(error)
            return

        if choice == 6:
            print('---> Search terminated by the holder.')
            return

        statementDict = {
            1 : 'Enter Transaction Type',
            2 : 'Enter Category / Source',
            3 : 'Enter Description',
            4 : 'Enter Amount',
            5 : 'Enter Transfer Account Number'
        }

        count = 0

        searchValue = input(f'{statementDict[choice]} : ').strip().title() if choice in (1 , 2 , 3) else input(f'{statementDict[choice]} : ').strip()

        if not searchValue:
            print(f'---> First {statementDict[choice]}.')
            return

        if choice == 4:
            amount , error = validateAmount(searchValue)

            if error:
                print(error)
                return

            amount = round(amount , 2)

        if choice == 1:

            for transaction in holderAccount['transactions']:

                if transaction['type'] == searchValue:

                    displaySearchResult(count , transaction)
                    count += 1

        elif choice == 2:

            for transaction in holderAccount['transactions']:

                if transaction['type'] in {'Income' , 'Expense'} and searchValue.lower() in transaction['category'].lower():

                    displaySearchResult(count , transaction)
                    count += 1

        elif choice == 3:

            for transaction in holderAccount['transactions']:

                if transaction['type'] in {'Income' , 'Expense'} and searchValue.lower() in transaction['description'].lower():

                    displaySearchResult(count , transaction)
                    count += 1

        elif choice == 4:

            for transaction in holderAccount['transactions']:

                if amount == transaction['amount']:

                    displaySearchResult(count , transaction)
                    count += 1

        elif choice == 5:

            searchAccNumber , error = self.validateAccNumber(searchValue)

            if error:
                print(error)
                return

            for transaction in holderAccount['transactions']:

                if (transaction['type'] == 'Transfer Out' and transaction['to'] == searchAccNumber) or (transaction['type'] == 'Transfer In' and transaction['from'] == searchAccNumber):

                    displaySearchResult(count , transaction)
                    count += 1

        print(f'''
------------------------------------------------

{f'{count} transaction(s) found.' if count != 0 else '---> No matching transactions found.'}
================================================
        ''')

    def filterTransactions(self):

        print('''
================ FILTER TRANSACTIONS ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        accNumber , error = self.validateAccNumber(inputAccNumber)

        if error:
            print(error)
            return

        holderAccount = self.accounts[accNumber]

        print(f'''
Account Holder : {holderAccount['name']}
Current Balance: ₹{holderAccount['balance']}

------------------------------------------------

Filter Transactions By:

1. Transaction Type
2. Category / Source
3. Amount Range
4. Balance Range

5. Back

------------------------------------------------
        ''')

        inputChoice = input('Enter the Choice : ').strip()

        choice , error = validateChoice(inputChoice , 1 , 5)

        if error:
            print(error)
            return

        if choice == 5:
            print('---> Filter terminated by the holder.')
            return

        statementDict = {
            1 : 'Enter Transaction Type',
            2 : 'Enter Category / Source',
            3 : 'Enter Amount Range : ',
            4 : 'Enter Balance Range : ',
        }

        count = 0

        if choice in {1 , 2}:

            searchValue = input(f'{statementDict[choice]} : ').strip().title()

        elif choice == 3:

            print(f'''
{statementDict[choice]}
            ''')

            minimumAmount = input('Starting Amount Value : ₹').strip()
            maximumAmount = input('Ending Amount Value : ₹').strip()

            startingValue , error = validateAmount(minimumAmount)

            if error:
                print(error)
                return

            endingValue , error = validateAmount(maximumAmount)

            if error:
                print(error)
                return

        elif choice == 4:

            print(f'''
{statementDict[choice]}
            ''')

            minimumBalance = input('Starting Balance Value : ₹').strip()
            maximumBalance = input('Ending Balance Value : ₹').strip()

            startingBalance , error = validateAmount(minimumBalance)

            if error:
                print(error)
                return

            endingBalance , error = validateAmount(maximumBalance)

            if error:
                print(error)
                return

            if startingBalance >= endingBalance:
                print('---> Starting value cannot be greater than ending value.')
                return

        if choice == 1:

            for transaction in holderAccount['transactions']:

                if transaction['type'] == searchValue:

                    displayFilterResult(count , transaction)
                    count += 1
        
        elif choice == 2:

            for transaction in holderAccount['transactions']:

                if transaction['type'] in {'Income' , 'Expense'} and searchValue.lower() in transaction['category'].lower():

                    displayFilterResult(count , transaction)
                    count += 1

        elif choice == 3:

            for transaction in holderAccount['transactions']:

                if startingValue <= transaction['amount'] <= endingValue:

                    displayFilterResult(count , transaction)
                    count += 1

        elif choice == 4:

            for transaction in holderAccount['transactions']:

                if startingBalance <= transaction['balanceAfter'] <= endingBalance:

                    displayFilterResult(count , transaction)
                    count += 1

    
        print(f'''
------------------------------------------------

{f'{count} transaction(s) found.' if count != 0 else '---> No matching transactions found.'}
================================================
        ''')

    def financialReport(self):

        print('''
================ COMPLETE FINANCIAL REPORT ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        print('''
------------------------------------------------
        ''')

        accNumber , error = self.validateAccNumber(inputAccNumber)

        if error:
            print(error)
            return

        holderAccount = self.accounts[accNumber]

        print(f'''
Account Holder   : {holderAccount['name']}
Account Number   : {accNumber}
Account Type     : {holderAccount['accountType']}
Current Balance  : ₹{holderAccount['balance']:.2f}

Report Status     : Complete

================================================
        ''')

        if not holderAccount['transactions']:

            print('''
---> No transactions recorded yet. 
            ''')
            return

        transactions = holderAccount['transactions']

        displayIncomeReport(transactions)

        displayExpenseReport(transactions)

        displayTransactionsSummary(self.openingBalance , holderAccount['balance'] , transactions)

    def accountStatistics(self):

        print('''
================ ACCOUNT STATISTICS ================
        ''')

        inputAccNumber = input('Enter Account Number : ').strip()

        accNumber , error = self.validateAccNumber(inputAccNumber)

        print('''
------------------------------------------------

        ''')

        if error:
            print(error)
            return

        accountDetails = self.accounts[accNumber]
        displayStatistics(accNumber , accountDetails)

    def displaySaveUI(self):

        accountsToSave = len(self.accounts)
        totalTransaction = 0

        for acc in self.accounts:
            totalTransaction += len(self.accounts[acc]['transactions'])

        print(f'''
================ SAVE DATA ========================

------------------------------------------------

                DATA BACKUP

------------------------------------------------

Accounts to Save       : {accountsToSave}

Total Transactions     : {totalTransaction}

------------------------------------------------

Account Summary:
        ''')

        if accountsToSave == 0:

            print('''
No Acconts to save.
            ''')

            return

        count = 0

        for accNumber in self.accounts:

            credentials = self.accounts[accNumber]

            print(f'''
{count + 1}. {credentials['name']}
   Account Number : {accNumber}
   Transactions   : {len(credentials['transactions'])}
            ''')
            count += 1

        print('''
------------------------------------------------

This will save all account information,
balances, budgets and transaction history.

------------------------------------------------

Do you want to continue?

1. Yes, Save Data
2. No, Cancel

------------------------------------------------
        ''')

        inputChoice = input('Enter the Choice : ').strip()

        choice , error = validateChoice(inputChoice , 1 , 2)

        if error:
            print(error)
            return

        if choice == 2:
            displayCancellation()
            return

        saveToDatabase(self.accounts)

    def displayLoadUI(self):

        currentAccounts = len(self.accounts)
        totalTransaction = 0

        for acc in self.accounts:
            totalTransaction += len(self.accounts[acc]['transactions'])

        print(f'''
================ LOAD DATA ========================

------------------------------------------------

                RESTORE DATA

------------------------------------------------

Saved Data Information:

Accounts Stored       : {storedAccounts}
Transactions Stored   : {storedTransactions}

------------------------------------------------

Loading saved data will replace the
currently loaded account information.

Current Data:

Accounts Loaded       : {currentAccounts}
Transactions Loaded   : {totalTransaction}

------------------------------------------------

Do you want to continue?

1. Yes, Load Data
2. No, Cancel

------------------------------------------------
        ''')

        inputChoice = input('Enter the Choice : ').strip()

        choice , error = validateChoice(inputChoice , 1 , 2)

        if error:
            print(error)
            return

        if choice == 2:
            displayLoadCancellation()
            return

        import copy

        duplicateDetails = copy.deepcopy(self.accounts)

        duplicateDetails , error = loadFromFile(duplicateDetails)

        if not error:
            self.accounts = duplicateDetails

        
    def terminate(self):

        print("---> Program terminated successfully.")
    
bankAccount = FinanceManager()
bankAccount.run()
