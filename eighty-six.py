

def main():
    new_password = input("Enter a new password: ")
    new_password_bis = input("Enter it again: ")

    if new_password == new_password_bis:
        print("Thank you.")
    else: 
        if new_password.lower() == new_password_bis.lower():
            print("They must be in the same case.")
        else:
            print("Incorrect.")



if __name__ == '__main__':
    main()