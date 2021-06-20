from array import *
import random


def main():
    nums = array ("f", [])
    for i in range(5):
        nums.append(random.uniform(10, 100))
    
    num = int(input("Type in a number between 2 and 5: "))
    while num < 2 and num > 5:
        num = int(input("Try again typing in a number between 2 and 5: "))
    else:
        print(nums)
        for i in range(5):
            new_num = (nums[i] / num)
            print(round(new_num, 2))




if __name__ == '__main__':
    main()