

def main():
    num1 = int(input("Type in a number: "))
    num2 = 0#int(input("Type in a number: "))
    total = num1 + num2
    quest = "y"
    while quest == "y":
        num3 = int(input("Type in a number: "))
        total = total + num3
        quest = input("Do you want to add another number?(y): ")
    print(f"The total is {total}")














if __name__ == '__main__':
    main()