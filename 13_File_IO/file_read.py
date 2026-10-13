file = open(r"C:\Users\priya\Documents\Python\sample.txt","r")

#after open the file => the file return itself is a file object
#we can imagine file object as a => pointer, variable => which store the value of thst file

# so the "file" is a type of variable or pointer
# if we wan to do operation on our file we have to do on that file variable

#lets read our data from our file 
data = file.read()
print(data)
print(type(data))

file.close()

#this mode is the default mode if we not mention any mode then it is gonna be read mode by default 