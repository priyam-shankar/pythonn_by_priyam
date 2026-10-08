class Wallet:
    
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.__balance = balance

    #method to add money
    def add_money(self,amount):
        self.__balance += amount
        
    #method to spend money
    def spend_money(self,amount):
        self.__balance -= amount
        
    def show_balance(self):
        print(f"Current balance = Rs {self.__balance}")
        
wal1 = Wallet("Priyam",5000)
wal1.add_money(2000)
wal1.spend_money(1500)
wal1.show_balance()