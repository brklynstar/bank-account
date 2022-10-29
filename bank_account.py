class BankAccount:
    def __init__(self, full_name, account_number, balance):
       self.full_name = full_name
       self.account_number = account_number
       self.balance = balance
''' Defined a class BankAccount with an init function that
takes in 3 parameters, fullname, account_number and balance'''



#Deposit Method
def deposit(self,balance):
   deposit_amount = float(input("Deposit Amount: $"))
   self.balance += deposit_amount
   print("Amount Deposited: $", deposit_amount, "New Balance: $", balance)

''' Defined a deposit method with the parameter amount
that allows user to input a float and will add the amount 
to the balance and print a message "Amount deposited: $x.xx
New balance: $y.yy "
'''    
      
#Withdraw Method
def withdraw(self, balance):
    withdraw_amount = float(input("Withdraw Amount: $" ,withdraw_amount, "New Balance: $",  balance))
    if self.balance >= withdraw_amount:
        self.balance -= withdraw_amount
        print("Amount withdrawn: $", withdraw_amount, "New Balance: $", balance )
    elif withdraw_amount > balance:
        balance += 10    
    print("Insufficient funds. An overdraft fee of $10 has been applied to your account.")
    print("New balance with overdraft: $", balance)

'''Withdraw method with the parameter amount
that allows user to input a float and will subtract the amount 
from the balance and print a message "Amount withdrawn: $x.xx
New balance: $y.yy " If user withdraws greater than current balance,
an over draft fee of 10 is deducted from balance.
'''    

#Get Balance Function
def get_balance(balance):
    print("n\Hello loyal customer!n\ Your account balance is: $",balance)

''' Method to get balance function to print account balance message'''


# Add Interest Function
def add_interest():
    balance_with_interest = (balance, * 0.00083)

''' Method that adds interest to users balance
with a monthly rate of 0.00083'''

#Print Statement Function
''' Method that printes a message with the account name,
account number and balance'''

#3 Bank Accounts
customer_1 = BankAccount("Brooke Finister", )
customer_2 = BankAccount()
customer_3 = BankAccount()

# Calling functions with BankAccount object

customer_1.deposit()
customer_1.withdraw()
customer_1.display()
