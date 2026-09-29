'''
age = int(input("Enter the age:"))

if age >=18 :
    print("You can vote")
    print("You can drive")
else :
    print("you can't vote")    
    
    
color = input("Enter color:")

if color == "red":
    print("STOP")
elif color == "green" :
    print("GO")
elif color == "yellow":
    print("LOOK")
else:
    print("wrong color for traffic light")

age = int(input("enter age:"))

if (age < 13) :
    print("child")
elif(age >= 13 and age < 18) :
    print("teenager")
else :
    print("Adult")

username = input("Enter your username:")
password = input("Enter your password:")

if(username == "admin" and password == "pass") :
    print("Login successfully")
elif(username != "admin"):
    print("wrong username")
else :
    print("wrong password")

num = int(input("Enter a number:"))
if(num % 5 == 0):
    print(num, "is a multiple of 5")
else :
    print(num,"is not a multiple of 5")
'''

num = int(input("Enter number:"))

if(num % 2 == 0):
    print("EVEN")
else:
    print("ODD")