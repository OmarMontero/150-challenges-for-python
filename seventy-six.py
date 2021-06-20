



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
        print(party)

        





if __name__ == '__main__':
    main()