# Lab 2: Account Class (Balance Setter Control)
class Account:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid amount! Balance cannot be negative.")

if __name__ == "__main__":
    acc = Account(100)
    print("Current balance:", acc.balance)
    acc.balance = -50
    acc.balance = 200
    print("Updated balance:", acc.balance)
