"""
In Nesting we are going to use put if within an if and ask a follow up question to to one's
we have already asked.


Here is a simple programme which asks our user about their favourite programme and few more 
question.
"""

tvShow = input("What is your favourite tv show? ")

if tvShow == "peppa pig":
  print("Ugh, why?")
  
  faveCharacter = input("Who is your favourite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
    
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")


"""
In this code if user's favourite show is peppa pig then the programme asked the progrmme 
about his favourite character.
"""


####    Day 7 Challenge   ####

"""
Make a programme which asks some question to user and check whether user is a fake fan or not
"""


####  Solution    ####

print ("Fake Real Madrid fan finder 👀")
print ("-------------------------------")

team = input ("What's your favourite football club?")

if team == "Real Madrid":
  jude_position = input ("What is the position of Jude Bellingham?")
  if jude_position == "Attacking Midfield":
    jude_number = input ("what's his jersy number in Real?")
    if jude_number == "5":
      print ("Nice. You are a Real Madrid fan")
  else:
    print ("See! FAKE Real Madrid fan")
else:
  print ("See! FAKE Real Madrid fan")