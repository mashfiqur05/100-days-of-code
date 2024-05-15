"""
Day 24 Challenge

Let's build an infinity dice!

Create subroutines that will roll a dice with any number of sides (essentially as big of a number as you like). 
Write one subroutine with one parameter that allows us to call a function (such as rollDice).

Example:

Infinity Dice 🎲

How many sides?: 600
You rolled 532

Roll again? yes
You rolled 102

Roll again? no

"""


###     Solution    ###


import random

print ("Infinity Dice 🎲")
print ()

slides = int (input ("How many slides?: "))
playGame = "yes"

def rollDice (slides):
    print ("You rolled", random.randint(1, slides))
while playGame == "yes":
    rollDice(slides)
    playGame = input ("Roll again? ")