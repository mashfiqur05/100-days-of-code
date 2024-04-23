"""
A while loop allows your code to repeat itself based on a condition you set.
It is similar to an if statement in that you ask a question, and 
as long as the answer is true, the computer will repeatedly run the code.
"""

"""
In the code below, the variable is called counter and starts at zero.
 The while loop has the condition saying, "while the counter is less than ten do this..."
In this case, print the variable and then add +=1 to that variable.
 As long as variable is less than 10, the loop will repeat the code.
"""

counter = 0

while counter <= 10:   ### if codition is like this counter > 10. then code will not print anything
  print(counter)
  counter += 1      ### if counter is not incresed this loop will be infinite




            ####Challenge for day 15        ####

"""
Write a programme which asked to user which animal he likes and then programme will give a message
Programme will repeat the code untill user said to exit.

"""



        ####    Solution    ###

        
exit = ""

while exit != "yes":
  animal = input("What animal do you want?: ")
  if animal == "cow":
    print ("A cow goes moo")
  elif animal == "dog":
    print ("A dog goes woof")
  elif animal == "cat":
    print ("A cat goes meow")
  elif animal == "pig":
    print ("A pig goes oink")
  elif animal == "bears":
    print ("A bear goes growl")
  elif animal == "bees":
    print ("A bee goes buzz")
  else:
    print ("I don't know that animal")
  exit = input ("Do you want to exit?")