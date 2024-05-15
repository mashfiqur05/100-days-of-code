print ("Eleven times table")
for i in range (1, 11):
    print ("11 *", i, "=", i*11)
print()    

"""
Ask the user to list a starting number, ending number, and increment to use. 
Display an answer based on the users' answers

"""

print()
print ("List Generator")
print()
starting_number = int(input("What number do you want to start with? "))
ending_number = int(input("What number do you want to end with? "))
incre = int(input("How many should I add each time? "))
print()

for i in range (starting_number, ending_number, incre):
    print (i)