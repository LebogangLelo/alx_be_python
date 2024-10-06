class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance=initial_balance
        
    def deposit(self,amount):
            self.account_balance += amount
            #print(f"Deposited: ${amount}")
    
    def withdraw(self,amount):
         if amount <= self.account_balance:
              self.account_balance -= amount
              #print(f"Withdrew: ${amount}")
              return True
         else:
              return False
    
    def display_balance(self):
         print(f"Current balance: ${self.account_balance}")