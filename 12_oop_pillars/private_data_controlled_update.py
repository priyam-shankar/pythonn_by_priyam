class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        
    #method for withdrawal 
    def withdraw(self,amount):
        if amount <= self.__balance :
            self.__balance -= amount
        else :
            print(f"Insufficient Balance")
            
    #method to show balance 
    def show_balance(self):
        print(f"Available Balance = {self.__balance}")    
        
acc1 = BankAccount(5000)
acc1.withdraw(8000)
acc1.show_balance()

# BankAccount
# Concept:
# - __balance → private attribute
# - Direct access → ❌ Not allowed
# - withdraw() → updates the private balance
# - If the withdrawal amount is less than or equal to the balance → withdrawal is allowed ✅
# - If the withdrawal amount is greater than the balance → "Insufficient Balance" ❌
# - show_balance() → reads the private balance
# Topic: Private Data + Controlled Update + Validation 🔒