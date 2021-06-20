

def main():
    dictionary = {}
    for i in range(4):  
        
        name = input("Write a name: ")
        age = int(input("Type in an age: "))
        shoe_size = int(input("Type in a size: "))
        dictionary[name] = {"Age": age, "Shoe_ size": shoe_size} 
        
    user_name = input("Write a name from the array: ")
    print("Name", "    Age")
    for name in dictionary:
        
        print(name, "  ", dictionary[name]["Age"])
    


if __name__ == '__main__':
    main()