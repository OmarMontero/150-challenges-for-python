from array import *
import random




def main():
    nums = array ("i", [])
    for i in range(5):
        nums.append(random.randint(0, 150))
    print(nums)
    user_selection = int(input("Which number do you want to check: "))
    while user_selection not in nums:
        user_selection = int(input("Please, select a number from the array: "))
    else:
        for idx, i in enumerate(nums):
            if i == user_selection:
                print(f"The position of {user_selection} in the array is {idx + 1}.")
    



if __name__ == '__main__':
    main()