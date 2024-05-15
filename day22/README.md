## Libraries
<br>
Libraries are collections of code that other people have written.
We can use a library by writing import and then the library name.This should always be one of the first lines of code.
<br>
<br>
In the code below, I have created a variable, 'myNumber'. I am making it equal to a random number given to me by the randint (random integer) library. I add the lowest number (1) and the highest number (100) that can be picked and the computer will generate a number at random.
<br><br>

```python
import random
myNumber = random.randint(1,100)
print(myNumber)
```

## Common Errors

### Error with name
<br>
- Why is this code showing the error of "name not defined?"
<br><br>

```python
import random

myNumber = randint(1, 100)
print(myNumber)
```
This error is because of the way libraries work. The names of functions and variables in libraries may be similar to the names I chose for my functions and variables. The way to access functions and variables in other libraries is to put random. in front of the library name.

```python
import random

myNumber = random.randint(1, 100)
print(myNumber)
```
<br>

### Error with random numbers and loops

 - For this code, I want 10 random numbers between 1-100 printed out. Why is it printing the same number instead of ten different random numbers?
<br><br>
```python
import random

myNumber = random.randint(1, 100)
for i in range(10):
  print(myNumber)
  ```
The problem is when I am generating my random number, I am doing it before the loop. I am asking for one random number and then storing it in a variable. Then, I am saying to print out this random number 10 times. Nowhere in the loop am I asking for a new number each time. I need to rearrange the order of my code.

<br>

```python
import random

for i in range(10):
  myNumber = random.randint(1, 100)
  print(myNumber)
  ```
  Now, each time the loop resets, it will generate a new random number. Now I can generate 10 random numbers between 1-100.
