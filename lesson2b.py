# python dictionary
person={
    "firstname":"John",
    "lastname":"Doe",
    "age":25,
    "salary":50000
}
# print/show the output
print(person)

# print first name 
print(person["firstname"])

# print age
print(person["age"])

# adding a new item
person["gender"]="male"
print(person)

person["county"]="kilifi"
print(person)

# updating/changing values
person["firstname"]="Mary"
print(person)

person["salary"]="100,000"
print(person)

# delete/remove a key value pair 
# delete age
del person["age"]
print(person)

del person["lastname"]
print(person)