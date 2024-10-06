myString = "Hello Nadif.How are you?"
print (myString[0:5])   # Hello
print (myString[6:11])   # Nadif

# String name [st : end : number of character to move]
print (myString[0:5:2]) # Hlo

#mistake: slice can not be 0. 
print (myString[::-1])  # reverse the string. Output: ?uoy era woH.fidaN olleH

print (myString.split())    # ['Hello', 'Nadif.How', 'are', 'you?']