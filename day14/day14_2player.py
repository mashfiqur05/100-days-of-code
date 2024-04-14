###     Challenge for day 14    ###
"""
Write a programme which helps you to play rock, paper, scissor game.
But you have to ensure that whenever you use input, each player cannot see what the other player typed in 😉.

"""


###     Solution    ###

from getpass import getpass as input
print ("EPIC 🪨 📄 ✂️ BATTLE")
print ("Select your move (R, P or S)")
player1 = input("Player 1 > ")
player2 = input("Player 2 > ")
if player1 == "R" and player2 == "R":
  print ("It's a tie!")
elif player1 == "R" and player2 == "P":
  print ("Player 2 wins!")
elif player1 == "R" and player2 == "S":
  print ("Player 1 wins!")
elif player1 == "P" and player2 == "R":
  print ("Player 1 wins!")
elif player1 == "P" and player2 == "P":
  print ("It's a tie!")
elif player1 == "P" and player2 == "S":
  print ("Player 2 wins!")
elif player1 == "S" and player2 == "R":
  print ("Player 2 wins!")
elif player1 == "S" and player2 == "P":
  print ("Player 1 wins!")
elif player1 == "S" and player2 == "S":
  print ("It's a tie!")
else: 
  print ("Invalid Move!")