import random


def main():
    number = random.randint(1,10)
    answer = int(input("Type in a number:"))

    while answer != number:
        if answer < number:
            print("Oops, to low")
        else:
            print("Oops, to high")
        answer = int(input("Try again: "))
    print("Well done")






if __name__ == '__main__':
    main()