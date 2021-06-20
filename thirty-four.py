import math

def getting_areas():
    user= float(input("""Hello, lets get some areas! Choose one option: 
    1) Square.
    2) Trianfle. 
    
    Type in an option: """))

    if user == 1:
        side = float(input("Write the length of one of its sides: "))
        
        print(f"The area of a square with a {side}cm side is {side**2}.")
    
    elif user == 2:
        base = float(input("Type in the base: "))
        height = float(input("Write the height: "))

        print(f"The area of a triangle with base {base} and height {height} is {(base * height)/2}.")
    
    else: 
        print("The answer isn´t correct. Please choose one of the two option.")



if __name__ == '__main__':

    getting_areas()