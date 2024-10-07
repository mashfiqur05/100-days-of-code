print ("Website Rating🌟")

dictionary = {"name": None, "url": None, "desc": None, "rating": None}

for name in dictionary.keys():
  dictionary[name] = input(f"{name}: ")

for name, value in dictionary.items():
    print (f"{name}: {value}")
