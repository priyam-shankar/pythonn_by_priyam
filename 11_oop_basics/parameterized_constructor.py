#Parameterized Constructor 

#1. Class → 2. Constructor → 3. Attributes set → 4. Object create → 5. Data use
class Mobile:
    def __init__(self, mobile_brand,mobile_model,mobile_price):
        self.brand = mobile_brand
        self.model = mobile_model
        self.price = mobile_price
        
m1 = Mobile("Samsung", "S24", 60000)
m2 = Mobile("Apple", "iPhone 16", 70000)
m3 = Mobile("OnePlus", 12, 50000)

print(m1.brand,m1.model,m1.price)
print(m2.brand,m2.model,m2.price)
print(m3.brand,m3.model,m3.price)