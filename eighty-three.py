


def main():
    word = input("Type in a word in upper case: ")
    while word.islower():
        word = input("Type in a word in upper case: ")
    else:
        print("Brilliant")



if __name__ == '__main__':
    main()