
def main():
    sales_data = {"john": {"n" : 3056, "s" : 8463, "e" : 8141, "w" : 7643}, "tom": {"n": 4932, "s": 6235, "e": 5820, "w": 1854}, "anne": {"n": 5239, "s": 6789, "e": 8965, "w": 4651}, "rona": {"n": 3901, "s": 3654, "e": 6958, "w": 3216}} 
    print(sales_data)
    name = input("Choose a name: ")
    region = input("Select a region: ")
    print(sales_data[name][region])
    change = input("Do you want to change the sales figure?(y/n)")
    if change == "y" or change == "yes":
        new_value = int(input(f"Type in the new value. Reminder previus data {sales_data[name][region]}: "))
        sales_data[name][region] = new_value
    else: 
        print("Thank you.")
    print(sales_data[name])
if __name__ == '__main__':
    main()