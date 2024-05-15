# Subroutine

So far, when we wanted to repeat code, we have had to use loops or copy and paste code.

What if I told you there was a way to use code or call it and use it anytime anywhere??

That is a subroutine!!

A subroutine tells the computer that a piece of code exists and to go run that code again and again...

## Just like a recipe


Subroutines work like a recipe in a cookbook. If you want to know how to make a cake, you don't have to start from scratch every time. You can use a recipe to get the same quality each time.

## How do we define a subroutine?
A subroutine is defined by:
```
def (which stands for definition)
```
You need to give the subroutine a name (and just like with a variable, you can't have spaces).

**def subroutine name (argument)**

You need to add () even if there are no arguments followed by a colon :. The code needs to be indented.

- Let's roll a random number on a six-sided dice. Copy the code below and click run.

```python
def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)
  ```
### Why is nothing happening??

In this code, I have defined how to roll a dice (this is my recipe for rolling a dice), but I have not actually 'called' the program to run.

## Call the Subroutine

- We need to 'call' the code by adding one more line to our code with the name of the subroutine and the empty ():

<br>

```python
def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

rollDice()
```
<br>

# Common Errors
<br>

## Name error
👉 Why is this code not working?
```python
def print My Name():
  print("My Name is David")
print My Name()
```

Just like with variables, you cannot have spaces with subroutines (onlyCamelCase or_using_underscores).

```python
def printMyName():
  print("My Name is David")
printMyName()
```
<br>

## Syntax error

👉 What happens when you run this code? Can you spot the error?

```python
def countToFive:
  for i in range(1, 6):
    print(i)
countToFive()
```
You need to add () in the first line, even though there is no argument.
```python
def countToFive():
  for i in range(1, 6):
    print(i)
countToFive()
```
<br>

## What about this one?
👉 Don't be fooled. This error is different than the last example.

```python
def countToFive():
  for i in range(1, 6):
    print(i)
  countToFive()
```
When you call your subroutine, make sure it is NOT indented.

```python
def countToFive():
  for i in range(1, 6):
    print(i)
countToFive()
```
