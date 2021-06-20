import random


def main():
    names = ["omar", "jon", "pepitu", "posho"]
    ages = [35, 32, 45, 38]
    shoe_sizes = [41, 43, 45, 39]
    dictionary = {}
    for i in range(4):  
        
        name = random.choice(names)
        age = random.choice(ages)
        shoe_size = random.choice(shoe_sizes)
        dictionary[name] = {"Age": age, "Shoe_ size": shoe_size} 
    print(dictionary)    
    user_name = input("Select a person from the array to delete the file: ")
    print("Name", "    Age")
    valor = dictionary.pop(user_name)
    for name in dictionary:
        
        print(name, dictionary[name])
    



if __name__ == '__main__':
    main()