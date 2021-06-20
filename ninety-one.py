from array import *


def main():
    nums = array ("i", [2, 2, 50, 100, 13])
    print(nums)
    check = int(input("Type in a number from the array: "))

    print(f"The number {check} is {nums.count(check)} time(s) in the array.")



if __name__ == '__main__':
    main()