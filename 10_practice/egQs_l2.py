info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
]

#Qs.(A)  list all unique courses
# for names, course in info:
#     print(names, course)

# i create a empty set then i will add my courses in set => then i get my unique courses

'''
course_set = set() 
for tup in info:
    # print(tup)
    # print(tup[0])  #names
    # print(tup[1])  #course
    
    course_set.add(tup[1])
    
print(course_set)

'''


#Qs.(B) list student enrolled in english

'''

for tup in info :
    if (tup[1]) == "English":
        print(tup[0])
        
        
'''


#Qs.(C)  Create Dictionary(student, set of courses)

# so dictionary have two things ok : 1.key :which is gonna be student name
                                #    2.value : which is gonna be set of courses
# so first we creat a empty dictionary then we add key and their values as in set form 
#here 2 possible scenario is there 1. if the key i.e name not exist  => in dictionary by using update method we add the key i.e name of the students with creating a empty set in which course is added => then we also add the corresponding course of the name 
#                                   2. if names  exist  => direct add the coursesin the set                                             



#creat dictionary 
dict = {}

for name, course in info:
    if(dict.get(name) == None):
        dict.update({name : set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
        
print(dict)