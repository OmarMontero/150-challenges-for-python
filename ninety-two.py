from array import *
import random


def main():
    array_given = array ("i", [])
    array_user = array ("i", [])

    for i in range(5):
        array_given.append(random.randint(0, 100))
    for i in range(3):
        array_user.append(int(input("Type in a number: ")))
    array_given.extend(array_user)
    final_array = sorted(array_given)
    print(final_array)
    for i in final_array:
        print(i)


if __name__ == '__main__':
    main()