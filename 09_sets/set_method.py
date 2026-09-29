s = {1,2,2,2,3,3,5,5,6,7,8}
print(f"before adding set is {s}")


#add method
s.add(10)
print(f"after adding set is {s}")

#remove method 
#set_name.remove(the element you want to remove)

#clear method
#set_name.clear(clear all the set)

#pop method
#set_name.pop() = > remove any random elements

#union and intersection method 

s1 = {1,1,2,3,3,4,5,6,7}
s2 = {6,6,7,8}
print(f"given set1 is = {s1}")
print(f"given set 2 is = {s2}")

print(f"after taking union on set1 and set2 = {s1.union(s2)}")
print(f"after taking the intersection between set 1 and set2 = {s1.intersection(s2)}") 