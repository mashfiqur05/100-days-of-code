print ("🌟Contact Card🌟")
name = input ("Input your name > ").strip().capitalize()
birthDate = input ("Input your date of birth > ").strip()
phone = input ("Input your telephone number > ")
email = input ("Input your email > ")
address = input ("Input your address > ").strip().capitalize()
contact = {"name": name, "birthDate": birthDate, "phone": phone, "email": email, "address": address}

print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["birthDate"]}""")
print(f"""Tel: {contact["phone"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")