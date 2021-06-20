

def main():
    nums = []
    for i in range(3):
        number = int(input("Type in a number: "))
        nums.append(number)
    more_numbers = input("Do you want to add another number? type it in or write no to exit. ")
    while more_numbers != "no":
        int(more_numbers)
        nums.append(more_numbers)
        more_numbers = input("Do you want to add another number? type it in or write no to exit. ")
    else:
        nums.pop()
        print(nums)
        print("Thank you for this beautiful comedy")


     







if __name__ == '__main__':
    main()