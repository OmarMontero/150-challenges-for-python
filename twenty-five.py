name = input("type in your name: ")

if len(name) >= 5:
    print(name.lower())
else:
    surname = input("Write your surname: ")
    print(name.upper()+surname.upper())
    

