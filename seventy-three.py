

def main():
    foods = {}
    for i in range(4):
        foods[i] = input("Write one of your favourites food: ")
    print(foods)
    
    dislike = int(input("Which one do you want to get rid of? "))
    del foods[dislike]
    print(sorted(foods.values()))
    #print(foods)
    

if __name__ == '__main__':
    main()