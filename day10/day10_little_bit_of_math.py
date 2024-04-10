adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)



###     Challenge for Day 10        ####

"""
Write a programme which will asked to user for resturant bill and percentage for tip and 
number of people then calculate the amount evrey person have to pay equaly divide .
print it in round figure

"""



####        Solution        ###

print ("Tip Calculator")

myBill = float(input("What was the bill?: "))
tip = int(input("What percentage do you want to tip?: "))
numberOfPeople = int(input("How many people?: "))

tip_amount = myBill * (tip / 100)
myBill += tip_amount    ## myBill = myBill + tip_amount
answer = myBill / numberOfPeople
answer = round(answer, 2)
print ("You each owe $", answer)