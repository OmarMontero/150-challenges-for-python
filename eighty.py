

def main():
    name = input("What´s your name?: ")
    print(f"Your name has {len(name)} letters.")
    surname = input("What´s your surname?: ")
    print(f"Your surname has {len(surname)} letters.")
    print("*" * 50)
    full_name = (name + " " + surname)
    print(full_name)
    print(len(full_name))
    



if __name__ == '__main__':
    main()