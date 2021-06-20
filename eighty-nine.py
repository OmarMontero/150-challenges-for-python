from array import *
import random

def main():
    new_array = array ("i", [])
    for i in range(5):
        new_array.append(random.randint(0,150))
    for i in new_array:
        print(i)


if __name__ == '__main__':
    main()