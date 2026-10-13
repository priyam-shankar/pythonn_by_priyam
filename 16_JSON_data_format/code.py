import json

json_str = '{"name": "Priyam", "isTeacher": true}'

#want to convert it in py_obj  => loads.()

py_obj = json.loads(json_str)

print(type(py_obj), py_obj)


#wanted to convert it in json from python object => dumps()