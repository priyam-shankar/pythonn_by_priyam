class Calculator:
    
    @staticmethod
    def add(a, b):
        return a+b

print(Calculator.add(10,20))


class Laptop:
    storage_type = "SSD"
    
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
        
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price * discount / 100)
        print(f"discounted price = {final_price}")
        
l1 = Laptop("16gb","512gb")
l1.calc_discount(40000,50)

# Laptop.calc_discount(40000,50)  => either you call it by the class or by the object 