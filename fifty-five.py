import random



def main():
    number = random.randint(1, 5)
    answer = int(input("Type in a number: "))
    if answer == number:
        print("Well done")
    else:
        if answer > number:
            print("Too high")
        else:
            print("Too low")  
    answer2 = int(input("Try with another number. ")) 

    if answer2 == number:
        print("well done")
    else:
        print("You lose")

    print(f"The number is {number}.")



if __name__ == '__main__':
    main()