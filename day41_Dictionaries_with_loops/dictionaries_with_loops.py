myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for i in myDictionary:
  print(myDictionary[i])

for value in myDictionary.values():
  print(value)

for name,value in myDictionary.items():
  print(f"{name}:{value}")

