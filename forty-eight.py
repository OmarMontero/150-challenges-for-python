


def main():

    count = 0
    guest_list = []
    more_guests = "y"
    while more_guests == "y":
        guest = input("Do you want to invite someone to the party? Write the guest´s name: ")
        print(f"{guest} has been invited to the party.")
        more_guests = input("Do you want to invite somebody else? (y/n): ")
        guest_list.append(guest)
        count += 1
    print(f"You have invited the bellow {count} guests to your party:")
    print(guest_list)


















if __name__ == '__main__':
    main()