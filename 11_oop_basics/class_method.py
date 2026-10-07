class BankAccount:
    bank_name = "SBI"
    
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
        
    @classmethod
    def change_bank_name(cls, bank_name):
        cls.bank_name = bank_name
        
acc1 = BankAccount("Priyam",5000)
acc2 = BankAccount("Palak",8000)

BankAccount.change_bank_name("HDFC")
        
print(acc1.bank_name)
print(acc2.bank_name)


class Laptop:
    storage_type = "SSD"
    
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
     
    @classmethod   
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")
        
    def get_info(self):     
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")       
        
l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

Laptop.get_storage_type()