myname = input ("What's your name?")
if myname == "Nadif":
  print ("Welcome Dude!")
  print ("You're just the baldest dude I've ever seen")
else :
  print ("Who on earth are you?!")


###     Common Mistake        ###

### Don't forget to use double equals in conditions
### Don't forget to use colon ':' after the conditions
### After an if-else and colon the next line should be intented furthur than before one




"""
Challenge of day 5
  
ask some question and match a hero like this

Marvel Movie Character Creator
--

Do you like hanging around? : no
Then you're not Spider-man

Do you have gravelly voice? : no
Aww,then you're not Korg

Do you often feel Marvelous? : yes
Aha! You're Captain Marvel! Hi!


"""

###     Solution    ###
print ("Marvel Movie Character Creator")
print ("--")

question1 = input ("Do you like hanging around? ")
if question1 == "no":
  print ("Then you're not Spider-man")
  question2 = input ("Do you have 'gravelly' voice? ")
  if question2 == "no":
    print ("Aww,then you're not Korg")
    question3 = input ("Do you often feel 'Marvelous'? ")
    if question3 == "yes":
      print ("Aha! You're Captain Marvel! Hi!")
  if question2 == "yes":
    print ("You're Korg!!")
if question1 == "yes":
  print ("Then you're Spider-man!")
else:
  print ("Hmmm maybe you're not fit to be a Hero afterall.")