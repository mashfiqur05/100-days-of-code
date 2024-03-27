"""
Concatenation is a complicated word that means glue together bits of text and variables
to make nice full sentences that look good in your output 
"""


myName = input ("What's your name? ")
myLunch = input ("What are you having for lunch? ")
print (myName, "is going to be chowing down on", myLunch, "very soon!")

####  Common error  #####
### don't forget to use comma
### don't use quotes in variable name



### challenge for Day 3  ###

"""
print the text like this and take user input
Name a food: >> Mac and Ceese
Name a plant: >> Cactus
Name a method of cooking:  >> 
burnedFood = input ("What word describes burned food? ")
item = input ("Name a DIY item: ")

print ("MENU")
print (methodCooking, food, "with", burnedFood, plant, "on a bed of", item)
"""
food = input ("Name a food: ")
plant = input ("Name a plant: ")
methodCooking = input ("Name a method of cooking: ")
burnedFood = input ("What word describes burned food? ")
item = input ("Name a DIY item: ")

print ("MENU")
print (methodCooking, food, "with", burnedFood, plant, "on a bed of", item)