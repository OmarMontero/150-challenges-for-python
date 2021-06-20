import math

def square_root():
    num = float(input("Type in a number over 500: "))
    sqr_num = math.sqrt(num)
    print(round(sqr_num, 2))




if __name__ == '__main__':
    square_root()