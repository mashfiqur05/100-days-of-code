for counter in range (10):
    print (counter)


"""
Make a programme that calculate your loan $1000 over 10 years 
at 5% APR.
At last also print the total amount you have paid in 10 years.
"""


print ("Lan Calculator")
print ("$1000 over 10 years at 5% APR")
payment = 1000
for year in range (10):
    payment += (payment * .05)
    print ("Year ", year+1, " is ", round (payment, 2))

print ("You have paid $", round (payment-1000, 2), "in interest!")