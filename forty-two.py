

def main():
    total = 0
    for i in range(5):
        number = int(input("Type in a number: "))
        question = input("Do you want to add this number to the grand total?(yes/no): ")
        if question == "yes":
            total = total + number
        else:
            pass
    print(total)





if __name__ == '__main__':
    main()