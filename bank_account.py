
#Define a Bank Account Class

class BankAccount:
    def __init__(self, full_name, account_number, account_balance):
        account_balance = 0
        self.name = full_name
        self.account = int(account_number)
        self.balance = float(account_balance)

    def greeting(self):
        print("\n\n$$$$$$ The Hustlers Bank ATM $$$$$$\n")

    def print_statement(self):
        print(f'Account Holder Name: {self.name}\nAccount No.:{self.account}\nCurrent Balance: ${self.balance}\n')

    def sign_off_statement(self):
        print(f'Thank you for coming thru and using the Hustlers Bank ATM!\nImma hold onto your cash for you!\n\nKeep stackin them racks {self.name}!\nStay Loyal.')  

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print(f'Deposit Amount: ${deposit_amount}' f'\nBalance after Deposit: ${self.balance}\n')

    def withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount
        print(f'Amount Withdrawn: ${withdraw_amount}\nBalance after Withdraw: ${self.balance}\n')
        if withdraw_amount >= self.balance:
            print(f'***Insufficent Funds***\n\n'f'Snatching $10 from you for that!\nAccount Balance with overdraft fee: ${self.balance - 10}\n\nDO NOT let that happen again {self.name}!\n\n')
      
    def get_balance(self):
        print(f'\nHello {self.name}!\nYour current account balance is: ${self.balance}\n')

    def add_interest(self):
        self.balance = (self.balance * 0.00083) + (self.balance)
        print(f'Account Balance after monthly interest: ${self.balance}\n')
    
    
    
  
#------------------------------------------------------------------------------------------  

# Bank Accounts:
#Deposit and withdraw with insuffcient funds
johnny_citizen = BankAccount('Johnny Citizen', '0193832756', 0)
johnny_citizen.greeting()
johnny_citizen.get_balance()
johnny_citizen.print_statement()
johnny_citizen.deposit(1200)
johnny_citizen.withdraw(1300)
johnny_citizen.sign_off_statement()


jane_citizen = BankAccount('Jane Citizen', '0157462548', 0)
jane_citizen.greeting()
jane_citizen.get_balance()
jane_citizen.print_statement()
jane_citizen.deposit(10000)
jane_citizen.withdraw(10)
jane_citizen.sign_off_statement()

mitchell_hudson = BankAccount('Mitchell Hudson', '0137295747', 0)
mitchell_hudson.greeting()
mitchell_hudson.get_balance()
mitchell_hudson.print_statement()
mitchell_hudson.deposit(400000)
mitchell_hudson.add_interest()
mitchell_hudson.withdraw(150)
mitchell_hudson.sign_off_statement()
