import datetime

class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.amount = 0

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount -= amount

    def print_account(self):
        print(f'Account number: {self.number}')
        print(f'Amount: {self.amount} {self.currency}')


class SavingsAccount(BankAccount):
    def __init__(self, number, currency, interest=0, dates_of_deposit=()):
        super().__init__(number, currency)
        self.interest = interest
        self.dates_of_deposit = dates_of_deposit
        
    def deposit(self, amount):
        today=datetime.date.today()
        if today.day in self.dates_of_deposit:
            super().deposit(amount)
        else:
            print(f'Today is {today}, you can deposit money only on {self.dates_of_deposit}')

class CreditAccount(BankAccount):
    pass


if __name__ == '__main__':
    sa=SavingsAccount(12345, 'USD', interest = 3, dates_of_deposit=[1,6,10,17])
    sa.deposit(500)
    sa.print_account()