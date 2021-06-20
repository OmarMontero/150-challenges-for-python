def main():
    data_set = [ [2, 5, 8],[3, 7, 4],[1, 6, 9],[4, 2, 0] ]
    print(data_set)
    user_row = int(input("Type in the row´s number: "))
    print(data_set[user_row - 1])
    user_addition = int(input("Type in a number to add: "))
    data_set[user_row - 1].append(user_addition)
    print(data_set[user_row - 1])



    


if __name__ == '__main__':
    main()