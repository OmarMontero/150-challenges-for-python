def main():
    data_set = [ [2, 5, 8],[3, 7, 4],[1, 6, 9],[4, 2, 0] ]
    print(data_set)
    user_row = int(input("Type in the row´s number: "))
    row = user_row - 1
    print(data_set[row])
    user_column = int(input("Wich column do you want to display? : "))
    column = user_column - 1
    print(data_set[row][column])
    answer = input("Do you want to change this value?(y/n) ")
    if answer == "y" or answer == "yes":
        new_value = int(input("Type in a new value: "))
        data_set[row][column] = new_value
    print(data_set)


if __name__ == '__main__':
    main()