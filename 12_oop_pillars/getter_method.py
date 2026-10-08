class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.__cgpa = cgpa
        
    #method to get cgpa 
    def get_cgpa(self):     #getter method
        return self.__cgpa
    
s1 = Student("Priyam",7.8)
#s1.print(f"cgpa = {get_cgpa()}")    # here we can't write like beacuse we write s1.print  => but print() is not the object method
#object's method ==> get_cgpa()
print(f"cgpa is : {s1.get_cgpa()}")


# **Remember in one line:**

# A **getter is a method that reads the value of a private attribute and returns it, so that we can safely access that value outside the object.**

# And bro, the **real power of a getter is `return`** — printing is not the job of a getter.

# A getter **returns the value**, and then we can use that returned value anywhere we want, such as:

# - `print` it
# - store it in a variable
# - use it in a calculation
# - compare it with another value

# **Example:**

# ```python
# def get_cgpa(self):
#     return self.__cgpa
# ```

# Here, `get_cgpa()` does not print the CGPA.

# It simply **returns the CGPA value** to the place where the method was called.