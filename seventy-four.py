

def main():

    colours = ["black", "white", "red", "blue", "yellow", "green", "purple", "orange", "brown", "grey"]
    bottom =  int(input("Type in a number between 0 and 4: "))
    top =  int(input("Type in a number between 5 and 9: "))
    print(colours[bottom:top])



if __name__ == '__main__':
    main()