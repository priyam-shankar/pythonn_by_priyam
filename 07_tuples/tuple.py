#tuples are list but they are immutable data types
# immutable sequence of values : at index we can't change the values 
# we can create tuples by using () => parenthesis


#lets create a numbers of tuples

tup = (1,4,2,7,5,"abc",3.14)
print(tup)
print(type(tup))
print(len(tup))

#tup[2] = 10    #'tuple' object does not support item assignment

#print(tup)

#creating single value tuples
tuple = (1)  # we can't create single value tuple as like that
# because python doesn't interpret this as a tuple it interprets as the value wriiten in the tuple

# eg tuple = (1) ; here in parenthesis the number is written is 1 so it interprt whole things to a int value you also check the type 

print(type(tuple))

# if you want to create single value tuple then you have to put a comma 

palak = (23,)
print(type(palak))

# same slicing process in tuple also 

print(tup[0:4])