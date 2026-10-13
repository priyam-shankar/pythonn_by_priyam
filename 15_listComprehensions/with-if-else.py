#label numbers as even and odd from range 1 to 6
#list comprehension using if - else
# syntax - [true_things  if condition   else false_thing  for loop with range]


labels = [f"{x}-Even" if x % 2 == 0 else f"{x}-odd" for x in range(11)]
print(labels)