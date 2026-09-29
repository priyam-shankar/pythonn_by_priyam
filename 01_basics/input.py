username = input("enter your username:")
print("welcome", username)


a = input("enter the number a:")
b = input("enter the number b:")

sum = a+b
print(sum)  #output => 105 not 15 
# beacuse the input function take anything in the form of string => so we have to change the type

x = float(input("enter x:"))
y = float(input("enter y:"))

sum = x+y
print(sum)

# Calculate the avergae of two numbers
p = float(input("enter 1st number:"))
q = float(input("enter 2nd number:"))

avg = (p+q) / 2

print("avg of two numbers is:", avg)