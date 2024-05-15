# What can range really do?
<br>
Give range one number, and it will count up to that number. However, you can actually give the range function a few options...

<br>

- **starting value :** what number do you want to start with?

- **ending value :**  the number after the number you want to end with (example: if you type 10 as the ending value, the computer will count until 9)

- **increment :** How much should it increase by every time it loops? (example: Do you want to count by 1s, 5s, 10s?)

## range ( starting value, value to end before, increment )
The ending value has an unsaid 'less than'. Meaning the computer will stop one number before the ending number that is written in the range.
<br><br>

**Let's try some examples.** 

## Increments

We know that this range will start at **0**  and continue to **999,999**  (which is the number right before the ending value written). The number will increase in **increments of 25**  each time.
```python
for i in range (0, 1000000, 25):
  print(i)
  ```

## Counting Backward

In this example, we are starting at **10**  and **counting backward**  to 0 (because 0 is what comes right before the ending value listed), and **counting backward 1**  each time.
```python
for i in range(10, -1, -1):
  print(i)
```
<br><br>
## Common Errors
```python
for i in range (10, 0):
  print(i)
```
The third value in the range function, increment, is missing. We need to add an increment of -1 to go backward. Without the increment written, the computer does the default of +1.

Without the increment listed, we are telling the computer: **start at 10, keep going until 0, and add one each time.** This can't be done so nothing will run unless we add an increment.

Here is the write code
```python
for i in range (10, 0, -1):
    print (i)
```

