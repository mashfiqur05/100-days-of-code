"""
Day 23 Challenge

1.Create a subroutine with both a username and password.
2.Create a loop to prompt the user again and again until they put in the correct login information.

Replit Login System

What is your username?: david
What is your password? whatAmazingHairYouHave

Whoops! I don't recognize that username or password. Try again!

What is your username? david
What is your password? baldies4life

Welcome to Replit!

"""

### Solution ###

def login():
    while True:
        username = input ("What is your username?: ")
        password = input ("What is your password? ") 
        if username == "Nadif" and password == "Hell0n4d1f":
            print("Welcome Nadif!")
            break
        else:
            print("That is not the correct username or password. Try again!")
            continue
    
print("REPLIT LOGIN SYSTEM")
login()