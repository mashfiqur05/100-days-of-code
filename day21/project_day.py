"""
Test your family and friends on their multiplication knowledge (or just be really mean to people you know and ask them to work out their multiplication tables for 5,474,000,000....)

1.Prompt the user by asking for a multiplication table for the number of their choice.

2.Generate the multiplication table for 1 to 10 times that number and ask each math fact as a question
(psst...that's a hint).

3.If the user gets the math correct, award them a point. If they get it wrong, do not give them any points.

4.At the end of the 10 rounds, show the user their score out of 10 for how many math facts they got correct.

5.Why not give users an emoji if they get all 10 math facts correct?

"""


print ("Math Game")
print()
multi = int (input ("Name your multiples: "))
print()
cnt = 0
for i in range (1, 11):
    correct_ans = multi * i
    print (i, "x", multi)
    ans = int (input (">"))
    if correct_ans == ans:
        print ("You got it right!🥳")
        cnt += 1
    else:
        print("That's not correct. It should have been", correct_answer)

if cnt == 10:
  print("Wow! A perfect score! 🥳")
else:
  print("You got", cnt, "out of 10 correct.")

