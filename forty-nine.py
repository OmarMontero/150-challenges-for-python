


def main():
    compnum = 50
    count = 0
    guess = 0

    while guess != compnum:
        guess = int(input("Which number do you think is compnum?: "))
        count += 1
        if guess < compnum:
            print("Oh, it´s too low")
        if guess > compnum:
            print("Oh, it´s too high")
        
    print(f"Shit! You did It. I dind´t expect that in {count} attempts, coming from you.")




















if __name__ == '__main__':
    main()