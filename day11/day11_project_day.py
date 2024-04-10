###     Project for day 11

"""
Calculate how many second in a year

60 second in 1 minute 
60 minute in 1 hour 
24 hour in a day
manth are different length .you need to do some math

12 month in a year


is it leap year? +1 day

"""


###     Solution        ###

year = int (input ( "Enter a year: "))

total_second = 365 * 24 * 60 * 60

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print ("Leap year")
      total_second += (24 * 60 * 60)
    else:
      print ("Not a leap year")
  else:
    print ("Leap year")
    total_second += (24 * 60 * 60)
else :
  print ( "Not a leap year")

print ("Total second of the year is", total_second)