# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# print(x)
# print(type(x))

# # parse x:
# y = json.loads(x)
# print(y)
# print(type(y))
# # the result is a Python dictionary:
# print(y["age"])

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))



# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(type(x))
# y = json.dumps(x, indent=4, separators=(". ", " = "))
# print(y)
# print(type(y))


# import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)


import re

# txt = "The rain in Spain"
# x = re.findall("ml", txt)
# print(x)


# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start())
# print(type(x))
# print("The first white-space character is located in position:", x.end())


# txt = "The rain in Spain"
# x = re.sub("\s","*", txt)
# print(x)
# print(type(x))

# complete details are on the website regex or official documentation of python

import camelcase