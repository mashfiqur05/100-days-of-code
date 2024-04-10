"""
Now that you have learned so much, your debugging skills are just getting better and better each day. 
Part of the fun of programming is finding that problem and squashing those bugs.
I have given you a few programs and all of them have a significant problem. 
Your job is to run the program, identify from the error message where the errors are, and fix them. 
(HINT: Hit run again to see if the code is no longer broken).

I'll be honest, some of these programs have multiple errors.
Let's get to squashing those bugs!

"""

"""
Fix this code 


print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?)
ans1 = ("What language are we writing in?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈
ans2 = input("Which lesson number is this?")
if(ans2>12):
print("We're not quite that far yet")
else:
  print("We've gone well past that!")
elif(ans2==12):
  print("That's right!")


"""


###     Final code after debugging

print ("100 Days of Code QUIZ")
print()
print("How many can you answer correctly?")
ans1 = input ("What language are we writing in?")
if ans1 == "python":
  print("Correct")
else:
  print("Nope🙈")
ans2 = input("Which lesson number is this?")
if ans2 > "12":
  print("We're not quite that far yet")
elif(ans2=="12"):
  print("That's right!")
else:
  print("We've gone well past that!")