"""
If statements support more than ==. They support inequality symbols as well. 
Remember those <, >, and = signs you used in math way back when? Well they are back again, but this time they look a bit different.
This is because the way input works behind the scenes is it always assumes what you are typing is text (or a string) and gets stored as a variable in "".

Casting is where we explicitly tell the computer that what we are typing is a number and not a letter.

"""

### The code below is saying any score greater than 100,000 is a winner. Anything less, try again.

"""
myScore = input("Your score: ")
if myScore > 100000:
  print("Winner!")
else:
  print("Try again 😭")

"""

### We crashed it! How do we tell the computer, "Wait, thats a number!"?

myScore = int (input ("What is your score?"))
pi = float ("3.1416")
if myScore > 100000:
  print ("Winner!")
else:
  print ("Try again")

if pi == 3.1416:
  print ("Right")
else:
  print ("Wrong")

### Here is shown casting in 2 ways.


###     Common Errors       ###

"""
Don't type like this 

myScore = int (input ("What is your score?")
forget to close the bracket

"""

