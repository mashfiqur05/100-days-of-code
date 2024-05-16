"""
Day 27 Challenge
Welcome to your first video game creation. You will create a video game that creates a character's health and attack stats...along with an epic name for your character.

Do not delete today's code. You will be building upon it on Day 28.

Write a subroutine that generates a character: first name and character type (human, imp, wizard, elf, etc.).
Write a subroutine that multiplies a bunch of random dice rolls together to generate the character's health stats. Use this formula:


Write a second subroutine that multiplies a bunch of random dice rolls together to generate the character's strength stats. Use this formula:


Present the data in a menu with time.sleep and os.system("clear") to make it appealing.
Wrap it in a loop so the user has the option to create another character.
Example:

Character Builder
Name Your Legend:
Sheila the Almighty
Character Type (Human, Elf, Wiard, Orc):
Human
Sheila the Almighty
HEALTH: 40
STRENGTH: 26
May your name go down in Legend...
"""


#Solution


import random, os, time

def rollDice (slides):
    result = random.randint(1, slides)
    return result

def characterHealth ():
    legend_health = ((rollDice (6) * rollDice (12)) / 2) + 10
    return legend_health

def characterStrenght ():
    legend_strength = ((rollDice (6) * rollDice (8)) / 2) + 12
    return legend_strength

while True:
  print("⚔️  CHARACTER BUILDER ⚔️")
  print()
  name = input("Name your Legend:\n")
  type = input("Character Type (Human, Elf, Wizard, Orc):\n")
  print()
  print (name)  
  health = characterHealth()
  print ("Health:", health)
  print()
  strength = characterStrenght()
  print ("Strenght:", strength)
  print()
  print("May your name go down in Legend…")
  print()
  again = input("Again?:\n")
  if again=="No" or again=="no":
    break
  time.sleep(1)
  os.system("clear")