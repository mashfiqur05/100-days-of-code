
"""
###     Day4 challenge      ###

Build a custom story for custom user like this

=== Your Adventure Simulator ===
You'll be asked a bunch of questions then we'll make you up an amazing story with YOU as the

name = input ("Your name: ")
enemy = input ("Your worst enemy's name: ")
superpower = input ("Your super power: ")

Our story begins as our hero name approaches a foreboding castle...
Suddenly a bolt of lighting striked the ground at the feet of, name
Our final battle begins! shouts the evil, enemy, clearly missing the fact that, name, has the power of, superpower, which means they'll win quite easily

"""



###     Solution    ###

print ("=== Your Adventure Simulator ===")
print ("""You'll be asked a bunch of questions then we'll make you up an amazing story with YOU as the""")
print()
name = input ("Your name: ")
enemy = input ("Your worst enemy's name: ")
superpower = input ("Your super power: ")
print ()
print ("Our story begins as our hero name approaches a foreboding castle...")
print ("Suddenly a bolt of lighting striked the ground at the feet of", name)
print ("'Our final battle begins!' shouts the evil", enemy, "clearly missing the fact that", name, "has the power of", superpower, "which means they'll win quite easily")



####    Sneaky Extra Skill 

print ("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m","for being a bad, bad person.")  ## Check README file for explation.
