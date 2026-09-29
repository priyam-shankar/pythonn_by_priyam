# dictionary => key value pair data type
# dictionary , we can write it by using semi brackets
# in dictionary the left side is the KEY  & all the KEY are the unique
#in the right side of the colon , the key has it value

# when we use dictionary: when we have a collection of multiple variables and we want to store it in a once 
# for eg: lets we wants to store some information of a student


info = {
    "name" : "palak",
    "cgpa" : "5.9",
    "subjects" : ["maths, science"],
    3.14 : "pi"
}

print(info)
print(type(info))

print(info["name"])
print(info[3.14])

#dictionary is mutable + unordered a=> it can change

info["cgpa"] = 6.1

print(f"after change the cgpa {info["cgpa"]}")