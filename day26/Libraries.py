import os, time

print("Welcome")
print("to")
print("Replit")

time.sleep (3)

os.system("clear")
username = input("Username: ")
print ("Username", username)


### Day 26 Challenge
"""
Play a song from this repl and build a menu to go with it. Make it look like an iPod!

Use a while true loop to create a title for a music player.
Allow the user to select to play a song and use subroutine called 'play' when they select the song.
Give the user the option to exit the program.
The title should pop up and pause along with the menu options.
If the user chooses anything else, start again by clearing the screen.
Use this code to get started:

from replit import audio
import os, time
def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    input()
while True:
  # clear the screen 
  # Show the menu
  # take user's input
  # check whether you should call the play() subroutine depending on user's input
Here is an example:

🎵 MyPOD Music Player
Press 1 to Play
Press 2 to Exit
Press anything else to see the menu again.
"""



## Solution

from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False 
  while True:
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : ")) # giving the user the option to stop playback
    if stop_playback == 2:
      source.paused = True
      return 
    else: 
      continue
  
while True:
  os.system("clear")
  print("🎵 MyPOD Music Player ")
  time.sleep(1)
  print("Press 1 to Play")
  time.sleep(1)
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else :
    continue
