# Challenge OOP (BankAccount)

class BankAccount:
    def __init__(self, account_number, owner_name):
        self.id = owner_name
        self.account = account_number
        self.balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You deposited: ${amount}")
            return True
        else:
            print("Deposit amount must be positive.")
            return False
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"You withdrew: ${amount}")
                return True
            else:
                print("Insufficient balance!")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False
    
    def transfer(self, amount, other_account):
        """Transfer money from this account to another account."""
        if self.withdraw(amount):
            other_account.deposit(amount)
            print(f"Transfer successful: ${amount} from {self.id} to {other_account.id}")
            return True
        else:
            print("Transfer failed.")
            return False
    
    def show_balance(self):
        print(f"Account owner: {self.id}, Balance: ${self.balance}")


# Example usage
user1 = BankAccount("11", "Yacoub")
user1.deposit(150)
user1.withdraw(50)
user1.show_balance()   

user2 = BankAccount("12", "Hanna")
user2.deposit(250)
user2.withdraw(230)
user2.show_balance()

# Transfer money
user1.transfer(100, user2)

# Show balances after transfer
user1.show_balance()
user2.show_balance()