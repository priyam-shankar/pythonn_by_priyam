notes = open(r"C:\Users\priya\Documents\Python\notes.txt","w")

data = "My name is Priyam.\nI am learning Python File I/O.\nToday I learned how to write data into a file."
notes.write(data) 

print(data)    
 
notes.close()