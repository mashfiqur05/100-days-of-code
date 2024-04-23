"""
We are going to build a "Guess the Number" guessing game.
You are going to use a while loop and some of the concepts from the past few days.
Start by picking a number between 0 and 1,000,000. This will be your first variable.
Create a while loop to keep asking the user to guess your number.
If they are too low, tell them "too low." If they guess too high tell, them "too high."
If the user guesses correctly, tell them they are a winner (maybe add a fun emoji too!)
Count the number of attempts it took for the user to guess number. 
Make sure you only show that after they get the answer correct.
Extra challenge: If the user types a negative number, exit program.

"""



### Solution ###
print ("Welcome to Guess the Number game🥳🥳🥳")
print ("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high,")
count = 0
while True:
  number = int(input("What is your guess?: "))
  if number == 500000:
    print ("Correct!")
    count += 1
    break
  elif number < 0:
    print ("You've guessed negative number")
    exit()
  elif number < 500000:
    print ("Too low")
    count += 1
    continue
  elif number > 500000:
    print ("Too high")
    count += 1
    continue
  else:
    print ("That is not a number I recognize.")
    count+= 1
    continue

print ("It took you", count, "guesses to get it correct!")

