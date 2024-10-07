print ("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")

beast = {"name": None, "type": None, "move": None, "hp":None, "mp": None}

for name in beast.keys():
    beast[name] = input (f"{name}: ").strip().title()

if beast["type"]=="Earth":
  print("\033[32m", end="")
elif beast["type"]=="Air":
  print("\033[37m", end="")
elif beast["type"]=="Fire":
  print("\033[31m", end="")
elif beast["type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for name, value in beast.items():
    print (f"{name}: {value}")