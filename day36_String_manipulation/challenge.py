nameList = []

def printList():
    for i in nameList:
        print (i)
    print()

while True:
    firstname = input ("Enter your first name: ").strip().capitalize()
    lastName = input ("Enter your last name: ").strip().capitalize()
    
    name = firstname + " " + lastName
    if name not in nameList:
        nameList.append(name)
    else :
        print ("Error. Duplicate name")

    printList()
