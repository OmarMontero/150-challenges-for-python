import random

def main():
    colours = ["red", "green", "blue", "black", "white"]
    colour = random.choice(colours)
    print(colours)
    user = input("Choose a colour...  ")
    #answer = user.upper()
    if user == colour:
        print(f"Well done. The number was {user}")
    else:
        if colour == "red":
            print("You should be getting angry RED.")
        elif colour == "green":
            print("I bet you are GRREN of envy.")
        elif colour == "blue":
            print("You are probably feeling BLUE right now.")
        elif colour == "black":
            print("I see a BLACK future for you.")
        else:
            print("Yes, your face is getting WHITE.")
        user2 = input("Choose a colour  ")
        if user2 == colour:
            print(f"Well done! The colour was {user2}")
        #answer2 = user2.upper()
        while user2 != colour:
            print("Try again")
            user2 = input("Choose a colour  ")
        print("BYE!")

            


        

if __name__ == '__main__':
    main()