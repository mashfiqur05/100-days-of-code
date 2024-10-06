name = input ("What's your name? ")
if name.lower().strip() == "nadif":     # string.strip() removes all the spces.
    print ("Hello Nadif")
else :
    print ("Wrong name")

### No duplicates

myList = []

def printList():
    print()
    for i in myList:
        print (i)
    print()

while True:
    addItem = input ("Item > ").strip().capitalize()
    if addItem not in myList:
        myList.append (addItem)
    printList()

