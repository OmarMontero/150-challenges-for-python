from array import *


def main():
    new_array = array ('i',[])
    for i in range(5):
        new_item = int(input("Type in a number: "))
        new_array.append(new_item)
    new_array = sorted(new_array)
    print(new_array[::-1])




if __name__ == '__main__':
    main()