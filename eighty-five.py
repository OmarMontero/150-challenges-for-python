


def main():
    name = input("What´s your name? ")
    count = 0
    for i in name:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count = count + 1
        else:
            pass
        
    print(f"Your name has {count} vowels.")



if __name__ == '__main__':
    main()