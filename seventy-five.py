import random

def main():
    array = []
    for i in range(4):       
        array.append(random.randint(100, 999))
    for i in array:
        print(i)

    number = input("Type in the number to check its position: ")
    counter = 0
    for idx, i in enumerate(array):
        if i == number:
            counter =+ 1
            print(idx)
    
    if counter == 0:
            print("The number {} is not in the list".format(number))







if __name__ == '__main__':
    main()