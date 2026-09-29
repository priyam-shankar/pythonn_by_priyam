def hello():    #fnc definiton
    print("hello world")
    print("hello python")
    
hello()         #fnc call

#function definiton
def sum(a, b):    #parameters   
    s = a + b
    return s

# ans = sum(33, 33)   #arguments
# print(ans)   

print(sum(33,33))       


def find_avg(a,b,c):
    avg = (a+b+c) / 3
    return avg

print(find_avg(2,4,6))
