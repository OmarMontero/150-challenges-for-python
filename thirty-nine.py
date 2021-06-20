


def main():
    number = int(input("Type in a number (between 1-12): "))
    while number < 1 or number > 12:
        number = int(input("The number have to be between 1-12: ")) 
    else:
        for i in range(1,13):
            print(i, "x", number, "=", (i*number) )













if __name__ == '__main__':
    main()
