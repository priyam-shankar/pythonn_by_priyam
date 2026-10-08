class Employee:
    start_time = "10am"
    end_time = "6pm"
    
        
class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role
        

class Accountant(AdminStaff):
    def __init__(self, salary,role):
        super().__init__(role)
        self.salary = salary
        
        

acc1 = Accountant(25_000,"GUARD")
print(acc1.salary,acc1.role,acc1.start_time,acc1.end_time)


#multiple inheritance

class Teacher:
    def __init__(self, salary):
        self.salary = salary
        
class Student:
    def __init__(self,cgpa):
        self.cgpa = cgpa
        
        
class TA(Teacher, Student):
    def __init__(self, salary,cgpa,name):
        super().__init__(salary)
        Student.__init__(self,cgpa)
        self.name = name
        
        
ta1 = TA(15_000,7.8,"Priyam")
print(f"{ta1.name} {ta1.cgpa} {ta1.salary}")