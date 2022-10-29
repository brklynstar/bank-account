
#Define a Bank Account Class
class BankAccount:
    def __init__(self, full_name, account_number, account_balance,):
        account_balance = 0
        self.name = full_name
        self.account = int(account_number)
        self.balance = float(account_balance)

    def print_statement(self):
        print(f'{self.name}\nAccount No.:{self.account}\n Balance: ${self.balance}\n')

    def sign_off_statement(self):
        print(f'Thank you, {self.name}, for being a loyal customer!\n')  

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print(f'Amount Deposited: ${deposit_amount}' f'\nBalance after Deposit: ${self.balance}\n')

    def withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount
        print(f'Amount Withdrawn: ${withdraw_amount}\nBalance after Withdraw: ${self.balance}\n')
        if withdraw_amount >= self.balance:
            self.balance - 10
            print(f'Insufficent Funds. An overdraft fee of $10 will be applied to your account.\nNew Account with overdraft: ${self.balance}\n')
      
    def get_balance(self):
        print(f'\nHello {self.name}!\nYour current account balance is: ${self.balance}\n')

    def add_interest(self):
        print(f'Account Balance with Monthly Interest Fee: {self.balance * 0.00083}\n')
  
#------------------------------------------------------------------------------------------  

# Bank Accounts:

johnny_citizen = BankAccount('Johnny Citizen', '0193832756', 0)
johnny_citizen.get_balance()

johnny_citizen.deposit(1200)

johnny_citizen.withdraw(1300)

johnny_citizen.sign_off_statement()


# jane_citizen =

# mitchell_hudson =
