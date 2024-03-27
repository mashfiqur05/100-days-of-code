### Just taking user input.
input ("What's your name? :")


### variable name need to be meaningful and snake_case_is_the_way ans camelCaseIsNiceToo 
### variable shoudln't have space 
### variable is case sensitive. myage and myAge are not same.

myName = input ("What is your name?")
myAge = input ("How old are you?")
replit = input ("Do you like Replit?")
print (myName)  ### don't put the variable name in the quotes.like this print ("myName")
print (myAge)
print (replit)


### Challenge for Day#2

"""
Getting to know you!

What's your name?: 
What's your favourite food?: 
What's your favourite music?: 
Where do you live?: 

You are
user's name
You're probably hungry for
user's favourite food
you're definitely getting your groove on to
user's favourite music
living in the amazing
user's where he/she lives in

"""



####    solution    ####
print ("Getting to know you!")
myName = input ("What's your name?: ")
favouriteFood = input ("What's your favourite food?: ")
favouriteMusic = input ( "What's your favourite music?: ")
location = input ("Where do you live?: ")

print ("You are")
print (myName)
print ("You're probably hungry for")
print (favouriteFood)
print ("and you're definitely getting your groove on to")
print (favouriteMusic)
print ("living in the amazing")
print (location)