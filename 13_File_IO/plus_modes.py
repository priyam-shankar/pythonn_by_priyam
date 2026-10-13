file = open("plus_modes.txt","r+")
f = open("plus_modes1.txt","w+")

o = open("plus_modes2.txt","a+")

file.write("hii")
print(file.read())

f.write("123")
print(f.read())

o.write("123")
print(o.read())

file.close()
f.close()
o.close()
