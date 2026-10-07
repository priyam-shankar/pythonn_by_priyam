class BankAccount:
    def __init__(self,name,account_number,balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        
account1 = BankAccount("Priyam",7452366951,12365)
print(account1.name, account1.account_number, account1.balance)

account2 = BankAccount("bittu",7485266951,123)
print(account2.name, account2.account_number, account2.balance)

account3 = BankAccount("amit",7478966951,5963)
print(account3.name, account3.account_number, account3.balance)


# The main purpose of a constructor (__init__) is to
# automatically initialize the required data when an object is created.

# self refers to the current object.
# It is used to store the data inside that object.