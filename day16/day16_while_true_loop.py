

while True:     ## remember here 'T' is capital
  print ("This programme is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print ("Aww, I was having a good time 😭")  


###     Challenge for day 16        #####

"""
Write a programme that asked you to fill up a lyrics. 
After write the correct word it will say you how times you attemted

"""


####        Solution        ###
print("Fill-in the blank lyrics!")
print("(Type in the blank lyrics and see if you are as cool as me.)")

counter = 0;
while True:
  print("Never going to ______ you up.")
  answer = input("What is the missing word? ")
  if answer == "give":
    print("Well done! It only took you", counter, "attempts.")
    break
  else :
    counter += 1
    print("Nope, try again.")