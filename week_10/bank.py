class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check_negative(self, amount):
        if amount <= 0:
            print("Amount should be positive")
            return True
        return False

    def check_overpaid(self, amount):
        if amount > self.balance:
            print("Not enough money")
            print(f"Balance: {self.balance}")
            return True
        return False

    def deposit(self, amount):
        if self.check_negative(amount):
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.check_negative(amount):
            return
        if self.check_overpaid(amount):
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def transfer(self, amount, other_account):
        if other_account == self:
            print("Transfer cancelled")
            print("You cannot transfer to yourself")
            return
        if self.check_negative(amount):
            return
        if self.check_overpaid(amount):
            return
        self.balance -= amount
        other_account.balance += amount
        print(f"Transferred {amount} from {self.name} to {other_account.name}")
        print(f"{self.name} new balance: {self.balance}")
        print(f"{other_account.name} new balance: {other_account.balance}")

    def display_balance(self):
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")


Bill = BankAccount("Bill", 1000)
Anna = BankAccount("Anna", 500)

Bill.deposit(100)
Anna.withdraw(100)

Bill.display_balance()

Bill.transfer(250, Bill)
Bill.transfer(250, Anna)
