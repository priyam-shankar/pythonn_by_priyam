#using the properties & method from  one class to the another class is called inheritance
#resusing attributes & methods from a parent (Base) class 

class Employee:     # Parent class / Base class /Superclass
    start_time = "10am"
    end_time = "6pm"
    
    def change_time(self, new_end_time):
        self.end_time = new_end_time
    
# now we want to use inheritance properties so 
class Teacher(Employee):        #child class / derived class / subclass
    def __init__(self,subject):
        self.subject = subject
        

        
t1 = Teacher("Math")
t1.change_time("5pm")
print(f"{t1.subject}, start time is = {t1.start_time} end time is = {t1.end_time}")
#here even though in our teacher class we didn't create any start and end time attribute but phirbhi these attributes exists 
# beacuse all the attributes accessible in the child class 
#here the concept of protected comes in data hinding  :
    # in our parent class : one of attribute is private , but we want to give access to subclass in that case that attribute is PROTECTED
    #but which attribute we won't wanna to give access to subclass and have private in parent class => private
 
 
#wanted to perform inheritance 
class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role
        
staff1 = AdminStaff("President")
print(f"{staff1.role} : {staff1.start_time} {staff1.end_time}")




