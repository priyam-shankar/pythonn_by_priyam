class Mobile:
    def __init__(self,imei):
        self.__imei = imei
        
    def show_imei(self):
        print(self.__imei)
        # return self.__imei

m1 = Mobile(1233456789)
m1.show_imei()



class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
        
    def show_salary(self):
        print(self.__salary)
        
emp1 = Employee("Amit",50000)
print(emp1.name)
emp1.show_salary()