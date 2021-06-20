

def main():
    word = input("Type in a word: ")
    upside_down = word[::-1]
    for i in upside_down:
        print(i)


if __name__ == '__main__':
    main()