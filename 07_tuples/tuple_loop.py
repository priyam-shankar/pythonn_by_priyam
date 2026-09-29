tup = (1,8,4,19,3)

sum = 0
for val in tup:
    sum += val
print(f"sum of vals is {sum}")
    
    
#methods of tuple 

palak = (1,2,3,5,6,9,5)

#index method is used to return the 1st occurence of index
print(palak.index(5))

#tuple.count() => the total numbers of elements in the given tuple 
print(palak.count(5))