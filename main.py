import datetime


class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.amount = 0

    def deposit(self, amount):
        self.amount += amount
        print(f'Your balance of account {self.number} was updated: deposited {amount} {self.currency}')

    def withdraw(self, amount):
        self.amount -= amount
        print(f'Your balance of account {self.number} was updated: {amount} {self.currency}')


    def print_account(self):
        print(f'Account number: {self.number}')
        print(f'Amount: {self.amount} {self.currency}')

    def end_of_month(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, number, currency, interest=0, dates_of_deposit=()):
        super().__init__(number, currency)
        self.interest = interest
        self.dates_of_deposit = dates_of_deposit

    def deposit(self, amount):
        today = datetime.date.today()
        if today.day in self.dates_of_deposit:
            super().deposit(amount)
        else:
            print(f'Today is {today}, you can deposit money only on {self.dates_of_deposit}')

    def end_of_month(self):
        super().deposit(self.amount * self.interest / 100)
class CreditAccount(BankAccount):
    def __init__(self, number, currency, interest = 0):
        super().__init__(number, currency)
        self.interest = interest

    def end_of_month(self):
        if self.amount < 0:
            self.withdraw(abs(self.amount * self.interest / 100))


if __name__ == '__main__':
    sa = SavingsAccount(12345, 'USD', interest=3, dates_of_deposit=[1, 6, 10, 17])
    sa.deposit(500)
    sa.end_of_month()
    sa.print_account()

    ca = CreditAccount(5678, 'EUR', interest=5)
    ca.withdraw(100)
    ca.end_of_month()
    print('-' * 30)
    ca.print_account()

