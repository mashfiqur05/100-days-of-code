"""
Use Day 27's character generator for this project...to build an automated game battle system!

Add return functions to your character's health and strength statuses from Day 27's project.
Generate two different characters and store their data (health and strength stats, character type, name, etc.).
Use a while True loop to simulate those two characters battling.
Roll one six-sided dice for both characters. The character who rolls the higher amount wins that round.
The winner of that round (the one who rolled the higher number) will give damage to the other character by doing the following:
Find the difference between the strength of both opponents and add one.
Take that amount away from the loser's health.
At the end of each round, check the stats of each character to ensure neither of them have died yet.
When one character dies (they run out of health), declare a winner of the battle!
To keep this battle from looking hideous between rounds use time.sleep to pause between rounds os.system("clear") to ensure the screen clears between battles.
Extra points for the use of emojis, colors, or even sound code!

Example:

⚔️ BATTLE TIME ⚔️
Name your Legend:
Arthur the Magnificent
Character Type (Human, Elf, Wizard, Orc): 
Elf
Arthur the Magnificent
HEALTH: 13
STRENGTH: 18
Who are they battling?
Name your Legend:
Sheila the Almighty
Character Type (Human, Elf, Wizard, Orc): 
Human
Sheila the Almighty
HEALTH: 40
STRENGTH: 26
*clear screen here*
⚔️ BATTLE TIME ⚔️
The battle begins!
Arthur wins the first blow
Sheila takes a hit, with 8 damage
Arthur the Magnificent
HEALTH: 13
Sheila the Almighty
HEALTH: 32
And they're both standing for the next round!
*clear screen here*
⚔️ BATTLE TIME ⚔️
The battle continues!
Sheila wins round 2
Arthur takes a hit, with 8 damage
Arthur the Magnificent
HEALTH: 5
Sheila the Almighty
HEALTH: 32
And they're both standing for the next round!
*clear screen here*
⚔️ BATTLE TIME ⚔️
The battle continues!
Sheila wins round 3
Arthur takes a hit, with 8 damage
Arthur the Magnificent
HEALTH: -3
Sheila the Almighty
HEALTH: 32
Oh no Arthur the Mighty has died!
Sheila the Almighty destroyed Arthur the Magnificent in 3 rounds!
"""

### Solution

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

print("⚔️ BATTLE TIME ⚔️")
print()
c1Name = input("Name your Legend:\n")
c1Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
c1Health = characterHealth()
c1Strength = characterStrenght()
print (c1Name, "Health:", c1Health, "Strength:", c1Strength)

c2Name = input("Name your Legend:\n")
c2Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
c2Health = characterHealth()
c2Strength = characterStrenght()
print (c2Name, "Health:", c2Health, "Strength:", c2Strength)

round = 1
winner = None

while True:
  time.sleep(3)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")
  c1Dice = rollDice(6)
  c2Dice = rollDice(6)
  difference = abs(c1Strength - c2Strength) + 1
  if c1Dice > c2Dice:
    c2Health -= difference
    if round==1:
      print(c1Name, "wins the first blow")
    else:
      print(c1Name, "wins round", round)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round==1:
      print(c2Name, "wins the first blow")
    else:
      print(c2Name, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)

  print()
  print (c1Name)
  print ("Health:", c1Health)
  print (c2Name)
  print ("Health:", c2Health)

  if c1Health<=0:
    print(c1Name, "has died!")
    winner = c2Name
    break
  elif c2Health<=0:
    print(c2Name, "has died!")
    winner = c1Name
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    
time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")

