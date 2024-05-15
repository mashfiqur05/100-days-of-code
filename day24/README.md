# Parameters

I get it. So far, subroutines have been a bit underwhelming...

Let's put those subroutines to better use by sending them information using parameters and making them do different things based on different inputs.

If you change the ingredients in a recipe, you get a different kind of cake. Let's do that with subroutines.

In a subroutine, the () are for the argument (FYI argument is another word for parameter). These are the pieces of information we pass to the code. These can be variable names that are made up for the first time within the argument ().

Here is a simple subroutine that uses the argument to take in the name of an ingredient and expresses its opinion (quite strongly) about the ingredient that the user typed. For example, 'chocolate' is amazing, but 'broccoli'...not so much.

<br>

```py
def whichCake(ingredient):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
```
<br>

## How do we call the subroutine?

We call it in the same way as before. However, instead of leaving the () blank, we send the code a message.
```python
whichCake("chocolate")
```

<br>

## Adding More Arguments
We can have as many arguments as we want, separated by commas.
Now, this subroutine is expecting three arguments: ingredient, base, and coating:
```py
def whichCake(ingredient, base, coating)
```
<br>

**Let's update our code to now show all three arguments:**
```py
def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")
whichCake("carrot", "biscuit", "icing")
```

<br>

 **I could even ask the user to name an ingredient, base, and coating by adding:**

```py
def whichCake(ingredient, base, coating):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
  print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")
userIngredient = input("Name an ingredient: ")
userBase = input("Name a type of base: ")
userCoating = input("Fave cake topping: ")
whichCake(userIngredient, userBase, userCoating)
```

# Common Errors

## Invalid Syntax
<br>

```py
def biggerNumber(number1 number2):
  if(number1 > number2):
    print(number 1, "is bigger")
  else:
    print(number 2, "is bigger")
biggerNumber (18,332)
```
<br>
You need a ,. Remember, you have to add a comma in between each variable that you expect to be a parameter. You can have as many arguments as you want. Remember, though, if you create two arguments, you must also call two arguments.

<br>

```py
def biggerNumber(number1, number2):
  if(number1 > number2):
    print(number1, "is bigger")
  else:
    print(number2, "is bigger")
biggerNumber (18,332)
```

