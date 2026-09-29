'''
name = input("enter your name:")
age = int(input("enter your age:"))
print("Hello",name + ",","you are",age,"years old")




num = float(input("enter the decimal no:"))
integral_part = int(num)
fractional_part = num - integral_part
print("Integer part:", integral_part)
print("Fractional part:", fractional_part)



num1 = float(input("enter no:"))
num2 = float(input("enter no:"))

print("sum :",num1 + num2)
print("difference :",num1 - num2)
print("product :",num1 * num2)
print("quotient :",num1 / num2)



val1 = int(input("enter value:"))
val2 = int(input("enter value:"))
val3 = float(input("enter value:"))

val1 = float(val1)
val2 = float(val2)

average = (val1 + val2 + val3) / 3
print("Average is:", average)



num = input("enter number: ")
integral_num = int(num)
float_num = float(num)
string_num = str(integral_num)

print("Integer:",integral_num, type(integral_num))
print("float:",float_num,type(float_num))
print("string:",string_num,type(string_num))



x = 10 + 3 * 2 ** 2
print(x)



a = int(input("enter val1:"))
b = int(input("enter val2:"))

print("Before Swapping:")
print("first number is:",a)
print("second number is:",b, "\n")


temp = a  #using third variable
a = b
b = temp


a,b = b,a  #another way to swap in python

print("After Swapping:")
print("first number is:",a)
print("second number is:",b)



celsius_Temp = input("Enter temp:")
celsius_Temp = float(celsius_Temp)

fahrenheit_Temp = celsius_Temp*(9/5) + 32

print("Temperatur in fahrenheit:",fahrenheit_Temp)



radius = float(input("Enter the length of radius:"))
area = 3.14 * radius**2
print("Area is:",area)


principal = input("Enter the principal value:")
rate = input("Enter the rate :")
time = input("Enter the time taken:")

principal = float(principal)
rate = float(rate)
time = float(time)

simple_interest = (principal*rate*time) / 100

print("Simple interest is :",simple_interest)

'''