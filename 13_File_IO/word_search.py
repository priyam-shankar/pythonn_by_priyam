'''
with open("word.txt","r") as f:
    line_number = 0
    word = "Python"
    found = False
    
    for i in f:
        line_number += 1
        if(word in i):
            found = True
            print(f"{word} found, \nIn line no = {line_number}")
            
    #if (found == False):
    if not found:
      print("not found")
      
'''     
      
#another method 

data = True
line = 1
word = "Python"

with open("word.txt","r") as f:
    while data:
        data = f.readline()
        
        if(word in data):
            print(f"{word} found at line {line}")
            break
        
        
        line += 1