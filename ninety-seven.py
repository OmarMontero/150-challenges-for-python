

def main():
    data_set = [ [2, 5, 8],[3, 7, 4],[1, 6, 9],[4, 2, 0] ]
    print(data_set)
    user_row = int(input("Type in the row´s number: "))
    user_column = int(input("Type in the column´s number: "))

    print(f"You´ve choosen the {user_row}º row and the {user_column}º column. It is {data_set[user_row - 1][user_column - 1]}")

if __name__ == '__main__':
    main()