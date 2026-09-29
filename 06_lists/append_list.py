#to add an element to the list ---> use list

nums = [1, 2, 3, 5]
print(f"Before Append list are {nums}")

nums.append(8)

print(f"After append list are {nums}")

#insert at the middle 

nums.insert(2,9)
print(f"Inserting at the middle of the list: {nums}")

#also we use sort function for sorting 
nums.sort()
print(f"After increasing sorting the list are {nums}")

#decresing order 
nums.sort(reverse=True)
print(f"After decresing sorting the list are {nums}")

#reverse the whole list

nums.reverse()
print(f"After reversing the list are {nums}")