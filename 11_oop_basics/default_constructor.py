# Default / non-parameterized constructor
# It has only one parameter: self

class Laptop:
    def __init__(self):
        self.brand = "HP"
        self.ram = 8
        self.storage = 512
        
l1 = Laptop()
print(f"laptop is of brand {l1.brand} with ram {l1.ram} and have storage {l1.storage}")

#Limitation of default constructor: It cannot accept different initial values for different objects during object creation.