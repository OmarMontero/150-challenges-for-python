

def main():
    list = {}
    for i in range(4):
        name = input("Write a name: ")
        age = int(input("Type in an age: "))
        shoe_size = int(input("Type in a size: "))
        list[name] = {"Age": age, "Shoe_ size": shoe_size} 
    user_name = input("Write a name from the array")
    print(list[user_name])
if __name__ == '__main__':
    main()