from array import *


def main():
    user_array = array ("i", [])
    deleted_array = array ("i", [])
    for i in range(5):
        new_value = int(input("Type in a number: "))
        user_array.append(new_value)
    final_array = sorted(user_array)
    print(final_array)
    removed_item = int(input("Which value do you want to remove from the array?: "))
    if removed_item in final_array:
        deleted_array.append(removed_item)
        final_array.remove(removed_item)

    else:
        print("The number is not in array.")
    print(final_array)
    print(deleted_array)



if __name__ == '__main__':
    main()