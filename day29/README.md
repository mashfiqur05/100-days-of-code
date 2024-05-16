# The secrets of print
# Secret One: end
You can already create **print** statements like a boss, but there are a few things you can do to make them easier.

By default, at the end of every **print** statement, the computer clicks **'enter'**.

```py
for i in range(0, 10):
  print(i)
```
**Output**
```
0
1
2
3
4
5
6
7
8
9
```

## Add a space
```
print (varName, end = " ")
```
Let's tweak that code and see if we can get it to print with a space between each number instead of a new line. What do you notice?

```py
for i in range(0, 100):
  print(i, end=" ")
```

**output**
```
0 1 2 3 4 5 6 7 8 9
```
## Add a space and comma
What if we want to add a comma and a space? Let's try it by adding , to our argument.
```py
for i in range(0, 100):
  print(i, end=", ")
```

**Output**
```
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

You can try by adding a **new line, tab, or vertical tab**

# Secret Two: sep
## Color Changing with end...
can turn the colors on and off different bits of the code by using **end.**

```py
print("If you put")
print("\033[33m", end="") #yellow
print("nothing as the")
print("\033[35m", end="") #purple
print("end character")
print("\033[32m", end="") #green
print("then you don't")
print("\033[0m", end="") #default
print("get odd gaps")
```
Let's concatenate that same print statement:
```py
print("If you put", "\033[33m", "nothing as the", "\033[35m", "end character", "\033[32m", "then you don't", "\033[0m", "get odd gaps", end="")
```
Now you may notice that we are getting weird double spaces in between the different sections. Let's fix that!

## Color changing with sep...

Take this same code and change end to sep (short for separator) and add a space at the end of each string. What happens?
```py
print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")
```
```
print (varName, sep = "")
```
This is a much easier way **to control** spacing in random text or emojis too!

# Secret Three: Cursor

Did you think about **That GIANT white cursor...**

```py
import os, time
for i in range(1, 101):
  print(i)
  time.sleep(0.5)
  os.system("clear")
```

You can turn that off! It is just a sneaky print command.

```
print('\033[?25l', end="")
```
we can turn the cursor back on:
```
print('\033[?25h', end="")
```

```py
import os, time
print('\033[?25l', end="")
for i in range(1, 101):
  print(i)
  time.sleep(0.2)
  os.system("clear")

print('\033[?25h', end="")
```
