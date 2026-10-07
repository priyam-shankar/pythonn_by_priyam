# Instance method : Instance method is a method that works with the data/attributes of a particular object using self
class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
        
    def get_cgpa(self): #which object called it self assign to that current object ok 
        return self.cgpa
        
s1 = Student("Amit",9.7)
s2 = Student("rupak",8.7)
s3 = Student("priyam",8.4)

print(f"{s2.name} has cgpa = {s2.get_cgpa()}")


class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdrawal(self, amount):
        self.balance = self.balance - amount
    
    def show_balance(self):
        print(self.balance)
        

acc1 = BankAccount("Priyam",5000)
acc2 = BankAccount("Palak",8000)
        
acc1.deposit(2000)
acc1.withdrawal(1000)
acc1.show_balance()


class Laptop:
    storage_type = "SSD"
    
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
        
    #now we define a instance method to print information of laptop
    def get_info(self):     # this is a Instance Method = > beacuse there is a self parameter
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")        # see this method access => instance attributes + class attributes (by self parameter)
        
l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

l1.get_info()