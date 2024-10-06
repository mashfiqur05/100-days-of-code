### Project Day....

import random, os, time

listOfWord = ["naruto", "goku", "luffy", "tanjiro", "elric", "vegeta", "akashi"]

myWord = random.choice(listOfWord)

letterPicked = []
choiceLeft = 5

while True:
    time.sleep(1)
    os.system("clear")
    letter = input ("Choose a letter -> ").lower()

    if letter in letterPicked:
        print("You've tried that before")
        continue

    letterPicked.append (letter)

    if letter in myWord :
        print("You found a letter")
    else:
        print("Nope, not in there")
        choiceLeft -= 1

    allLetters = True
    print()
    for i in myWord:
        if i in letterPicked:
            print(i, end="")
        else:
            print("_", end="")
            allLetters = False
    print()

    if allLetters:
        print(f"You won with {choiceLeft} left!")
        break
    if choiceLeft <= 0:
        print(f"You ran out of lives! The answer was {myWord}")
        break
    else:
        print(f"Only {choiceLeft} left")

