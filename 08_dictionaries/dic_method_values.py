# dict_name.values() => gives  the only values of the key

info = {
    "name":"palak",
    "cgpa": 5.1,
    "dept": "Social Work",
    "age" : 31
}

dict_val = info.values()
print(dict_val)


#dict_name.items() => gives the key + pair value of dictionary
group = {
    "name" : "Engineer",
    "type" : "solo",
    "members" : 1
}

dict_items = group.items()
print(dict_items)

# we have get method => we use it to access the value of any particular key 
# we have 2 ways to access => 1. dict_name[key]  => you can get the value   2.by get method : dict_name.get(key)  => you can get the value 

school = {
    "name" : "G.I.P Public School",
    "type" : "C.B.S.E",
    "no of students" : 1400,
    "location" : "pawapuri"
}

print(school["type"])
#in the square notation if we write wrong key it through an error
#but in the get method if we write wrong key it prints none instead of giving error
print(school.get("location"))


#update method => to add new key value pair 
#eg:

school.update({
    "state" : "bihar"
})

print(school)