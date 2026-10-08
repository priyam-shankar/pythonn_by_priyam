#encapsulation: it is a process in which we bind the data and methods in a single unit along with controlling the access to the data 
# to implement the encapsulation = > python have 3 access levels  1.Public Member   2.Protected Member  3.Private Member

class BankAccount:
    def __init__(self,name,balance):
        self.name = name        #public
       # self.balance = balance  #public attribute  => we can 
       # self._balance = balance  => protected attribute
        self.__balance = balance    #after making private => called data mangling(if we want to access directly then we got error)

#if we make an attribute private then it is private => and if we want to access it then we have to access through getter and setter function
#getter and stter is normal function just for geeting and setting the private data we called geetter and setter 
#Because by use of function => if we access the data then it is safe in programming 
#so always get the data by function
    
    def get_balance(self):      #getter function
        return self.__balance
    
    def set_balance(self,newBalance):
        self.__balance = newBalance 
        
acc1 = BankAccount("Priyam",400_000)

acc1.set_balance(900_000)

print(f"{acc1.name}, balance is = Rs {acc1.get_balance()}")

# the private variable which we make it is not completely protected i.e if we want to access it we do :
# for this we have to write => obje_name.class_name__privatevariablename, eg : acc1.BankAccount__balance


