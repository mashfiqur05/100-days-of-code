"""
Project day 13

Make a programme which will ask your number and return your grade.
It will also gives you bonus mark if condition is matched

"""


###     Solution    ###


print ("Exam Grade Calculator")
print ("Name of exam: Computer Science")
print ("Max. Possible Score: 100")

score = int(input("What is your score?"))
          
last_digit = score % 10
if last_digit == 8:
  score += 2
elif last_digit == 9:
  score += 1

if score >= 90:
  print ("You got", score, "which is an A+")
elif score >= 85:
  print ("You got", score, "which is an A")
elif score >= 80:
  print ("You got", score, "which is an B+")
elif score >= 75:
  print ("You got", score, "which is an B")
elif score >= 70:
  print ("You got", score, "which is an C+")
elif score >= 65:
  print ("You got", score, "which is an C")
elif score >= 60:
  print ("You got", score, "which is an D+")
elif score >= 55:
  print ("You got", score, "which is an D")
elif score >= 50:
  print ("You got", score, "which is an D-")
else:
  print ("You got", score, "which is an F")