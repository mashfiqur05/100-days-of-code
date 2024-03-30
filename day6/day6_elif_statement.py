"""
elif statement allows us to ask more question and get more options in same code blocks.
That means I can say this or this or this and else.So I can have lots of specific different state.

 
"""


print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")
if username == "mark" and password == "password":
  print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
  print("Hey there Suzanne!")
elif username == "jo" and password == "jo123@98":
  print("Yo Jo!")
elif username == "jim" and password == "Jimmy":
  print("Hello Jim!")
else:
  print("Go away!")


###     Common errors      ####

### elif must go after the if and before the else.
### Same error occur that mentioned in if else statement 



###     Challenge for Day 5     ####
  
"""
Create a programme that have similar log in system. Ask to user to username and password and other quesris like this

MY LOGIN SYSTEM
++++++++++++++++
username = input("Username > ")
password = input("Password > ")

username == "David" and password =="fgh6868"
Hello David. Hope you enjoyed your bike ride in beautiful streets of Sydney
Create sales deck for xyz client. This gonna be another best one from you


do it for at least 3 people 

"""





###     Solution Day5       ###

print("MY LOGIN SYSTEM")
print("++++++++++++++++")
username = input("Username > ")
password = input("Password > ")
department = input("task for the day > ")

if username == "David" and password =="fgh6868" and department == "sales":
    print("Hello David. Hope you enjoyed your bike ride in beautiful streets of Sydney")
    print("Create sales deck for xyz client. This gonna be another best one from you")
elif username == "Mark" and password == "gh25toa" and department == "data analytics":
    print("Hi Mark, it's going to be hot day in New York, don't forget to drink loads of water")
    print("please work on player accuracy data. We want our team to win!")   
elif username == "Paul" and password == "127asd" and department == "Foodzone":
    print("Hi Paul, yesterday you left the kitchen clean, Good Job!")
    print("Prepare food as per the food chart. You are an awesome chef!")
else:
    print("Errr....I don't know you. Bye!")