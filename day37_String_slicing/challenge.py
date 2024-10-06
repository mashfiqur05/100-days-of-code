print ("🌟Star Wars Name Generator🌟")

firstName = input ("Input your first name > ")
lastName = input ("Input your last name > ")
maidenName = input ("Input your mother's maiden name > ")
cityName = input ("Input the city where you were born > ")

name = f"{firstName[:3].title()}{lastName[:3].lower()} {maidenName[:2].title()}{cityName[-3:]}"
print (f"Your Star Wars Name is {name}")