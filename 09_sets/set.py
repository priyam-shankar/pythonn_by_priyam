#set data types is a collection of unique elements
#set are mutable
#but the elements in the set are immutable
p = {1,2,2,2,3}
print(p)
print(type(p))
print(len(p))

#set are unordered
#we can also add the values in set 

p.add(7)
print(p)
print(len(p))

#if we want to create a empty set then it will be a dictionary not a set

empty_set = {}
print(empty_set)
print(type(empty_set))

#remeber one thing curly braces => creates dictionary and set but empty curly braces is the type of dictionay not the set
#for empty creating empty set  we have to write 
empty_sets = set()  # this is basically a constructor function
print(empty_sets)
print(type(empty_sets))