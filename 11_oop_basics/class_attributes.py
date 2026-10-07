#1. Class → 2. Constructor → 3. Attributes set → 4. Object create → 5. Data use

class Student:
    college = "Assam University Silchar"        # class attributes
    
    def __init__(self,name,age,branch):
        self.name = name            #instance attributes
        self.age = age
        self.branch = branch

class BankAccount:
    bank_name = "SBI"
    
    def __init__(self,name,account_number,balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        
        
s1 = Student("Priyam", 21, "ECE")
s2 = Student("Rahul", 22, "CSE")

print(f"{s1.name} {s1.age} {s1.branch} {Student.college}")
print(f"{s2.name} {s2.age} {s2.branch} {Student.college}")

print(s1.college)   # we can also access our class attribute through object 


acc1 = BankAccount("Priyam",12345678,852)
acc2 = BankAccount("Rahul",87654321,741)

print(f"{acc1.name} {acc1.account_number} {acc1.balance} {acc1.bank_name}")
print(f"{acc2.name} {acc2.account_number} {acc2.balance} {acc2.bank_name}")