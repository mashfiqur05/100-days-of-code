# Return Command
Let's go deeper into subroutines. Can they send information back to the main part of the program?

Let's do this with the return command.

**The return command sends some information back to the part of the code that called it. This means the function call is replaced with whatever was returned.**

### Pin Picker
This subroutine creates a random pin number for us. This subroutine **(called pinPicker)** has the parameter called **number** (how many numbers I want to have in this pin). Then, there is a string **(called pin)** that is empty and a for loop that is used to create a defined amount of random numbers. The variable **number** controls how many times the loop will add the new number to the pin. This is done through **+=** and concatenating new values. We will cast the random number as a string so it can be concatenated together.

```py
#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin
#4 means we want 4 random numbers
myPin = pinPicker(4) # myPin stores the number. 
print (myPin)
```

## Common Errors
### Nothing is happening
 What is the problem here? Why is nothing happening?
```py
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area
areaOfTriangle (5, 22)
```
We need to assign a variable to **areaOfTriangle** and **print** it out.
```py
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

area = areaOfTriangle (5, 22)
print(area)
```

### Name Error
Why is it saying area is not defined!? We see it inside the subroutine.
```py
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area
areaOfTriangle (5, 22)
print(area)
```
Variables that are created for the first time in a subroutine are only available inside that subroutine.
We cannot call the variable area outside the subroutine.
We need to create the variable area inside the subroutine.
```py
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

area = areaOfTriangle (5, 22)
print(area)
```