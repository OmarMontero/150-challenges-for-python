import random

def main():
    options = ["h", "t"]
    selected = random.choice(options)
    user = input("Choose either head or tail(h/t)  ")

    if user == selected:
        print("You win")
    else:
        print("You lose")

    print(selected)





if __name__ == '__main__':
    main()