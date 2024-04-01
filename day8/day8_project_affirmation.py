### Make a machine which give you a positive message by asking some question



print ("Custom Affirmation Generator")
print ("----------------------------")

name = input ("What's your name?")
day = input ("What day of the week is it?")
feeling = input ("How are you feeling?")
if name == "Nadif" or name == "nadif":
  if day == "Monday" or day == "monday":
    if feeling == "good" or  feeling == "Good" or feeling == "great":
      print ("Nadif just starting the week with that positive ernegy, amazing! You'll rock this week for sure!")
    elif feeling == "bad" or feeling == "tired" or feeling == "Bad" or feeling == "Exhausted":
      print('''Monday is the hardest day of the week, 
  but also just it's beginning! Take a moment for yourself, 
  drink a coffee and remember that you just gotta find the right attitude to rock it!''')
else:
  print ("I don't know you,", name, "but I hope you're having a great day! This", day, " will be your best ", day, "of the year")