## Dynamic Lists

Dynamic lists are ways of using a blank list and adding or removing items to it as we go.

## Blank lists
Let's make an agenda for today. I am not going to put anything in this list (yet). Behind the scenes, the computer is going to recognize this code as a blank list.
```
myAgenda = []
```
## Append a list
**.append** will let us add whatever is in **()** to the list

Let's use a while True loop to add items to the list. We will store this in a variable called item. Add this code to the end of the code above:
```py
while True:
  item = input("What's next on the Agenda?: ")
  myAgenda.append(item)
  printList()
```
## Printing our new list
Wait?! Why can't we see what we just added to the list? We need to print the list each time to see what has changed. Let's use a subroutine (why not!):
```py
myAgenda = []
def printList():
  print() #this is just to add an extra space between items
  for item in myAgenda:
    print(item)
  print() #this is just to add an extra space between items
while True:
  item = input("What's next on the Agenda?: ")
  myAgenda.append(item)
  printList()
```
```
#The comments in green are for you and the computer will skip them.
```

## Removing Items from a List
```py
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    myAgenda.remove(item)
  printList()
```
Notice how using .remove will remove what is inside the ( ).

## Common Errors

### Removing something that is not there
Add "recording" to your list when you hit run. Now, remove "nap." Yikes! An ugly error message.

```py
myAgenda = []
def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 
while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    myAgenda.remove(item)
  printList()
```

The error message is just saying "x not in list". What does that mean? The thing you asked to remove is not there. (i.e. You asked to remove a nap from a list that it was not added to in the first place). The best workaround is to add a nested `if` statement to your code:
```py
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    if item in myAgenda:
      myAgenda.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()
```

Why is this not working? What does that error even mean?
```py
myAgenda = []
def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 
while True:
  menu = input("Add or Remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    item.append(myAgenda)
  elif menu == "remove":
    item = ("What do you want to remove?: ")
    if item in myAgenda:
      item.remove(myAgenda)
    else:
      print(f"{item} was not in the list")
  printList()
```
The problem is with the `append` function. We have two objects backwards. The list name comes first and then what's being added to the list goes inside (). 

Hint: You will see the same issue with `remove` too.

It always needs to be: `listname.append()` or `listname.remove()`

```py
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("Add or Remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = ("What do you want to remove?: ")
    if item in myAgenda:
      myAgenda.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()
```