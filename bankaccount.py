class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
    
    def display_statement(self):
        print(f'Your account currently has ${self.balance:.2f}.')


# program introduction

print('Let\'s create an account')

name = input('Please enter the name of the owner: ').title()
balance = float(input('Please enter a starting balance: '))
account = BankAccount(name, balance)

print('Thank you - what  do you want to do with your account?')
quit = ''
while quit != 'Q':
    quit = input('To deposit press D, to withdraw press W, to print a statment press P, to quit press Q:').upper()

    if quit == 'D':
        amount = float(input('Please enter the amount to deposit:'))
        account.deposit(amount)
        account.display_statement()
    elif quit == 'W':
        amount = float(input('Please enter the amount to withdraw: '))
        account.withdraw(amount)
        account.display_statement()
    elif quit == 'P':
        account.display_statement()
    elif quit != 'Q':
        print('Unknown request - please try again.')

print('Done - final statement below: ')
account.display_statement()


    