

def main():
    number = int(input("How many people do you want to invite to the party: "))
    if number < 10:
        for i in range(number):
            name = input("What´s your friend´s name?: ")
            print(f"{name} has been invited")
    else:
        print("Too many people papi, It´s coronavirus time.")        















if __name__ == '__main__':
    main()