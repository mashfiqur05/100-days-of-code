my2DList = [ ["Jony", 21, "Mac"], 
             ["Nadif", 20, "Linux"],
             ["David", 24, "Windows"] ]

print (my2DList)    ## [['Jony', 21, 'Mac'], ['Nadif', 20, 'Linux'], ['David', 24, 'Windows']]
print (my2DList[0]) ## ['Jony', 21, 'Mac']
print (my2DList[0][2])  ## Mac

my2DList[2][2] = "Linux"
print (my2DList[2][2])  ## Linux