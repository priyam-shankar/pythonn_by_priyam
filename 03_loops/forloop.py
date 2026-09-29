# for loop is used for the sequential traversal
''' 
string = "Priyam"

#in => membership operator => used to check the presence
if 'a' in string:
    print("a is in the string")
else:
    print("a is not in the string")
    


for var in string:
    print(var)
    
'''

# range(n) => it means 0 to n-1 in python

# for i in range(4):
#     print(i)



#want to print hey priyam 5 times

# for i in range(5):
#     print("hey priyam")




# want to count the no of i's in the word 
# word = "artificial Intelligence"

# count = 0

# for ch in word:
#     if(ch == 'i'):
#         count += 1
        
# print("count of i = ", count)    

#count vowels 

word = "artificial"

count = 0

for ch in word:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count += 1
print("count of vowels is = ", count)