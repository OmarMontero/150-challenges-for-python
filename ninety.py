from array import *


def main():
    nums = array ('i', [])
    count = 0
    while count < 5:
        num = int(input("Type in a number: "))
        if num >= 10 and num <= 20:
            nums.append(num)
            count = count + 1
        else:
            print("Outside of range.")
    for i in nums:
        print(i)




if __name__ == '__main__':
    main()