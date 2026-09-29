# list is a built in data type in python : mutable sequence of values
#list is a type of array in python 
# in a list, indexxing is follow 
# for eg : we take the list of marks

marks = [98,95,94,87,80]
print(marks)
print(len(marks))
print(marks[4])

#we know that strings are immutuable => at particular index we can't change the value 
# but list are mutable 

marks[4] = 78
print(marks)

names = [1,4,7,3,9,"palak"]
print(names)
print(type(names))

# string ---> slice ---> substring (str[start_index : end_index])

#list ----> slice ----> sublist

mark = [99,89,100,65,92,"abc",100.2]
print(mark[0:2])
print(mark[:len(mark)])
print(mark[5:len(mark)])