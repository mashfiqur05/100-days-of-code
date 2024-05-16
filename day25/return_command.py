#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin
    
myPin = pinPicker(4) #4 means we want 4 random numbers
print ("Your pin is:", myPin)

###  Day 25 Challenge
"""
Let's extend Day 24's project and create a health stats generator for a character in a video game.

Create a subroutine that rolls a dice of any size and returns that number.
Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
Print out the character's health stats.
Add a loop to give the user the option to generate health stats for another character.
(We genuinely see this in video games!)

🥳 Extra points if you ask for the character's name and double extra points if you use different colors!

"""


### Solution

import random

def rollDice(slides):
  result = random.randint(1, slides)
  return result

def characterHealth ():
  roll_6 = rollDice (6)
  roll_8 = rollDice (8)

  health = roll_6 * roll_8
  return health

print ("⚔️Character stats generator⚔️")

haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = characterHealth()
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character?")

