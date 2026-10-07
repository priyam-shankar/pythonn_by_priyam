class Product:
    total_product = 0 
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.total_product += 1
    
    def get_info(self): #instance method
        print(f"price of {self.name} is Rs {self.price}")   
    
    @classmethod   
    def get_count(cls):     #class method 
        print(f"total products in store = {cls.total_product}")
         
    
    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (price * discount / 100)
        print(f"discounted_price = {final_price}")
        
        
p1 = Product("Mobile", 20_000)
p2 = Product("laptop",40_000)
p3 = Product("pen",10)

p1.get_info()
Product.get_count()
p1.calc_discount(p1.price,10)