myUser = {"name": "Nadif", "age": 20 }

print (myUser["name"])  # Nadif
print (myUser["age"])   # 20
print (myUser)  ## {'name': 'Nadif', 'age': 20}

## Changing the value
myUser["name"] = "Mashfiqur Rahman"
print (myUser["name"])  # Mashfiqur Rahman


### For f string we have to use this way
print (f"My name is {myUser['name']} and I am {myUser['age']} years old.")  ## My name is Mashfiqur Rahman and I am 20 years old.

