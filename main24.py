# DICTIONARY IN PYTHON 
# dict = {
#     1 : "vansh",
#     2 : "shreynash",
#     3 : "yash",
#     4 : "arjav",
#     5 : "anvi"
# }
# print(dict[4])   
info = {"name":"vansh", "age": 19, "eligible":True}
# print(type(info))
# print(info)  
# print(info.get("name2"))
# print(info["eligible"])
# print(info.keys())
# print(info.values())
 
# for key in info.keys():
#     print(f"the values corresponding to the {key} is {info[key]}")
print(info.items())
for key, value in info.items():
    print(f"the value of corresponding to the key {key} is {value}")