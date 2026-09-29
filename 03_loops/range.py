# range function generates the sequences of number
# range() contains 3 parametrs => range(start, stop, step)
# start => starting value, stop => stoping value , and it is very important , step => it is the updation value 
# start and step are the optional values but stop is the mandaratory balue 

# if we didn't pass start and step value => by default start value is 0 and step is update by +1

for i in range(5):
    print(i)
    
print("after 1st loop:")  
for var in range(1,6):
    print(var)
    
print("after 2nd loop:")

for val in range(1,10,2):
    print(val)
    
    
    
    
# sum of n natural numbers 

n = int(input("enter the number:"))

sum = 0

for k in range(1,n+1):
    sum += k
    
print("sum of n natural no is:",sum)