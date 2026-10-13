# here another mode is there i.e => readline 
#READLINE: readline reads the data line by line

file = open(r"C:\Users\priya\Documents\Python\sample.txt","r")


data = file.readline()      #so if we want to read the data by line by line =>> we use readline funtioon
print(data )

data = file.readline()
print(data )

data = file.readline()
print(data )

# why there is a next there in the output 
 
file.close()

#beacuse of the print function it automatically prints the next line