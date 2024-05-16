"""

👉 Day 30 Challenge
Create a program that uses a loop that asks the user what they have thought of each of the 30 days of challenges so far.

For each day, prompt the user to answer a question and restate it in a full sentence that is center aligned underneath the heading.

Example:

30 Days Down
Day 1: 
Amazing
            You thought Day 1 was amazing.
Day 2:
so good that I bought the David plushie
              You thought Day 2 was so good...
"""

### Solution


print("30 Days Down - What did you think?")
print()
for i in range(1, 31):
  thought = input(f"Day {i}:\n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print()