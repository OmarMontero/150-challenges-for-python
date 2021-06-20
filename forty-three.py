


def main():
    direction = input("Which direction do you want to count(up/down)?: ")
    number = int(input("Give me a number: "))
    if direction == "up":  
        for i in range(0, number + 1):
            print(i)
    elif direction == "down":
        for i in range(number , -1, -1):
            print(i)

    else:
        print("I don´t understand")














if __name__ == '__main__':
    main()