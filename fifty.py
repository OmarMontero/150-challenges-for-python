


def main():
    num = 0
    while num < 10 or num > 20:
        num = int(input("Tyoe in a number between 10 and 20: "))
        
        if num < 10:
            print("To low, papi")
        if num > 20:
            print("To highl, papá")
    print(f"{num} That´s righ!")










if __name__ == '__main__':
    main()