# Dictionary --> Dicyionaries are the ordered collection of data items. They Stores multiple items in a single variable. Dictionary items are in key value pairs that are seprated by commas and enclosed in curly brackets.
dic = {
    "Name":"Saurabh Digambar Chorge",
    "RollNo":45,
    "EmpId":1234
}
print(dic)

dic2 = {
    1:"Saurabh",
    2:"Shubham",
    3:"Amar",
    4:"Omkar",
    5:"Raj",
    6:"Pravin",
    7:"Laxman"
}
print(dic2)
print(dic2[4])
print(dic2.get(4)) # Throughs an error when key is not present

# Multiple keys() & values()
print(dic2.keys())
print(dic2.values())

# keys using for loop 
for key in dic2.keys():
    print(dic2[key])

# Accessing key-value pairs
print(dic2.items())

# using for loop
for key,value in dic2.items():
    print(f"Key {key} & value {value}")

