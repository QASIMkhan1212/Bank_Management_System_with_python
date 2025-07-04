# Custom exception for insufficient balance
class BalanceException(Exception):
    pass

# BankAccount class definition
class BankAccount:
    # Initialize account with initial amount and account name
    def __init__(self, Initial_Amount: int, Acc_Name: str):
        self.balance = Initial_Amount
        self.name = Acc_Name
        
    # Print the current balance of the account
    def get_balance(self):
        print(f" Account:{self.name} balance Rs.{self.balance:.2f}")
      
    # Deposit the given amount and update balance
    def deposit(self, amount):
        print(f"Previous Balance {self.balance}")
        self.balance = self.balance + amount
        self.get_balance()
        print(" Deposit Completed")  
  
    # Check if transaction amount can be processed
    def viable_transaction(self, amount):
        if self.balance >= amount:
            print(f"\n Total amount of {self.name}: {self.balance} and Rs.{amount} transferred")
        else:
            # Raise exception if balance is insufficient
            raise BalanceException(f"the Account :{self.name} has only a balance of Rs.{self.balance:.2f}\n")
  
    # Withdraw the given amount from the account
    def Withdraw(self, amount):
        try:
            self.viable_transaction(amount)  # Check if withdrawal is possible
            print(" Withdrawal Completed")
            self.balance = self.balance - amount  # Deduct amount from balance
            self.get_balance()
        except BalanceException as error:
            # Handle insufficient balance error
            print(f"withdraw interrupted due to {error}")
  
  
    def transfer(self, amount, other_account):
        try:
            print(" **** Transfer Begininning **** ")
            self.viable_transaction(amount)
            self.Withdraw(amount)
            other_account.deposit(amount)
            print(" **** Transfer Completed **** ")
        except  BalanceException as error :
            print(f"transfer interrupted due to {error}")
            
            
  
# Create two bank account objects

Qasim = BankAccount(1000, " Qasim")                             
kashif = BankAccount(1000, " kashif")  

# Try to transact amounts from both accounts

try:
    Qasim.viable_transaction(1000)
except BalanceException as error:
    print(error)

try:
    kashif.viable_transaction(1001)
except BalanceException as error:
    print(error)

# Uncomment below lines to test deposit and balance functions

Qasim.deposit(250)
kashif.deposit(300)

Qasim.get_balance()
kashif.get_balance()


Qasim.Withdraw(1000)
kashif.Withdraw(1001)

Qasim.transfer(1000, kashif)
kashif.transfer(1001, Qasim)
