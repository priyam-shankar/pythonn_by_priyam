# finally always executes => whther an exception occurs or not 
try:
    x = int(input("enter x :"))
    ans = 10 / x
    
except ZeroDivisionError:
    print(f"Divide by 0 is not allowed")
    
except ValueError:
    print(f"invalid literal for int()")

else:
    print(f"ans = {ans}")
    
finally:
    print("End of Program")
    
    

try:
    f = open("data.txt")
    print(f.read())
    
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution Completed")
