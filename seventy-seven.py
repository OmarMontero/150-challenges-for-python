

def main():
    party = []
    for i in range(3):
        party.append(input("Write the name of your guest: "))
    print(party)

    answer = input("Do you want to add another one? Type in the name. (Write no if you want to finish): ")
    
    while answer != "no":
        party.append(answer)
        answer = input("Do you want to add another one? Type in the name. (Write no if you want to finish): ")
        #party.append(answer)
    else:
        print(list(enumerate(party)))
        
    uid = int(input("Type in the ID of any guest: "))
    for idx, i in enumerate(party):
        if idx == uid:
            delete = input(f"Do you still want {party[idx]} to come to the party?(yes/no) ")
            if delete == "no":
                party.remove(i)
                
    print( "*" * 50)
    print("This is you final guest´s list:")
    print(party)
    print("Thanks for you visit. Visit helpingwithyourparty.com")

        





if __name__ == '__main__':
    main()