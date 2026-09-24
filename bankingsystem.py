from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    @abstractmethod
    def account_type(self) -> str:
        pass

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def display(self) -> None:
        print("Name:", self.name)
        print("Account Type:", self.account_type())
        print("Balance:", self.balance)


class SavingsAccount(Account):

    def account_type(self) -> str:
        return "Savings Account"


class CurrentAccount(Account):

    def account_type(self) -> str:
        return "Current Account"


# Create account
account = SavingsAccount("Haritha", 5000)

# Deposit money
account.deposit(2000)

# Display details
account.display()