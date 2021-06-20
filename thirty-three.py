def get_remainer():
    num1 = float(input("Write a number: "))
    num2 = float(input("Write another number: "))

    print(f"The result of {num1} divided by {num2} is {num1//num2} with {num1%num2} remaining")




if __name__ == '__main__':
    get_remainer()