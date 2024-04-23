### The continue command stops executing code in the loop and starts at the top of the loop again.
### Essentially, we want to kick the user back to the original question.
### Adding continue will start the code from the start and ask the first question again: "Do you go left or right?".
### The else statement refers to any input besides left or right (up or esc). Since the user is a winner, 
### we do not want to use break or it would say they have failed.


while True:
  print ("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print ("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print ("Ahh! You're a genius, you've won")
    exit()
print ("The game is over, you've failed!")

### exit command directly stop the command


### Commmon Error

### exit is a function after exit you have to put a parenthesis().

### Challenge for day 17

"""
Make the day 14 game for 3 round using break continue statement

"""


###     sOLUTION    ###
from getpass import getpass as input
print ("EPIC 🪨 📄 ✂️ BATTLE")

round = 1
player1_score = 0
player2_score = 0

while (round <= 3):
  if player1_score == 2 or player2_score == 2:
    break
  print ("Round", round)
  print ("Select your move (R, P or S)")
  player1 = input ("Player 1 > ")
  player2 = input ("Player 2 > ")

  if player1 == "R" and player2 == "R":
    print ("It's a tie!")
    continue
  elif player1 == "P" and player2 == "P":
    print ("It's a tie!")
    continue
  elif player1 == "S" and player2 == "S":
    print ("It's a tie!")
    continue
  elif player1 == "R" and player2 == "P":
    print ("Player 2 wins the round")
    player2_score += 1
    round += 1
    continue
  elif player1 == "R" and player2 == "S":
    print ("Player 1 wins the round")
    player1_score += 1
    round += 1
    continue
  elif player1 == "P" and player2 == "R":
    print ("Player 1 wins the round")
    player1_score += 1
    round += 1
    continue
  elif player1 == "P" and player2 == "S":
    print ("Player 2 wins the round")
    player2_score += 1
    round += 1
    continue
  elif player1 == "S" and player2 == "R":
    print ("Player 2 wins the round")
    player2_score += 1
    round += 1
    continue
  elif player1 == "S" and player2 == "P":
    print ("Player 1 wins the round")
    player1_score += 1
    round += 1
    continue
  else:
    print ("Invalid move")
    continue
if player1_score == 2:
  print ("Player 1 wins the game!")
elif player2_score == 2:
  print ("Player 2 wins the game!")

print ("Thanks for playing!")