# to return all the keys of the dictionary
# dict_name.keys() => print all the key names of the dictionary

info = {
    "name" : "palak",
    "cgpa" : "5.9",
    "subjects" : ["maths, science"],
    3.14 : "pi"
}

# print(info.keys())

#we can also put it in a varibale then print the variable
# dict_keys = info.keys()
# print(dict_keys)

#we can also typecast the dictionary into a list 

dict_keys = list(info.keys())
print(dict_keys)
print(type(dict_keys))