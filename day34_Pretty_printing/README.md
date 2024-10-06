# Pretty print Functions

Let's build a pretty `print` subroutine! So far all the subrouintes you have made have been pretty boring...just saying.

When we have a list of data, being able to print out that data in pretty ways is something we need to be able to do. So "pretty printing" is actually a thing.

I have created a program called "Spammer Inc." to spam emails (obviously this is not something you would actually do). If the user presses 1, they can add an email, and pressing 2 allows them to remove an email. (Hint: This should all look familiar so far).

```py
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") # start by clearing the screen
  print("listofEmail") # print the title of my program
  print() # print a blank line
  for email in listOfEmail: # use for loop to access list
    print(email)
  time.sleep(1)

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
    prettyPrint()  
  time.sleep(1)
  os.system("clear")
```

## Creating a Numbered List

I can also ensure my list prints as a numbered list. Let's make this happen by making these few changes below to our subroutine. This code snippet only shows the subroutine so we can focus on the changes there:

We still need to call the subroutine. Let's edit our while loop a bit.

```py
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  counter = 1 
  for email in listOfEmail: 
    print(f"{counter}: {email}") 
    counter += 1 
  time.sleep(1)
  
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3": # we added this elif
    prettyPrint() # called our subroutine here
  time.sleep(1)
  os.system("clear")
```

## Using the Index

We can also use loops in a slightly different way to access elements in a list (or array). With the way we have our code written right now, our list creates a variable called email, sets it equal to the first value (with our counter we set 1 as the first value), and then counts on as we go. (2, 3, 4, etc.)

However, we can also set the `for` loop to use the `index`. What should happen is `index` will start at 0, go through the entire code in the loop at 0, go back to the start of the loop, add 1, and then loop again and again until the list ends..

```py
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): # len counts how many items in a list
    print(f"{index}: {listOfEmail[index]}") 
  time.sleep(1)


while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  time.sleep(1)
  os.system("clear")
```   

`len` counts how many items are in a list. In this case, it is starting at 0 and then keeps going until it reaches the end of our data inside our list. We can now eliminate the counter variable because we are counting with index.

## Common Errors

**Can you figure out why this is crashing?**

```py
import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in len(listOfEmail): 
    print(f"{index}: {listOfEmail[Index]}") 
    counter += 1 
  time.sleep(1)


while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  time.sleep(1)
  os.system("clear")
```

**Answer**

- Make sure your operators are correct. Counter should be `+=` in order to create a numbered list.

- Look at your fstring. Are the brackets correct?

- Is your indent correct when you called `prettyPrint()`?
```py
import os, time
listOfFood = []
def prettyPrint():
  os.system("clear") 
  print("listofFood") 
  print()
  counter = 1 
  for order in listOfFood: 
    print(f"{counter}: {order}") 
    counter += 1 
  time.sleep(1)
while True:
  print("Yummy Food Restaurant")
  menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
  if menu == "1":
    order = input("order > ")
    listOfFood.append(order)
  elif menu =="2":
    order = input ("delete order> ")
    if order in listOfFood:
      listOfFood.remove(order)
  elif menu == "3": 
    prettyPrint() 
  time.sleep(1)
  os.system("clear")
```

