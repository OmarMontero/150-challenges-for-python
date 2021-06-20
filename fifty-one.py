

def main():
    num = 10
    
    while num > 0:
        print(f"""There are {num} green bottles hanging on the wall.
        {num} green bottles hanging on the wall and 
        if 1 green bottle should accidentally fall.""")
        num = num - 1
        answer = int(input("How many green bottles will be hanging on the wall?  "))
        if answer == num:
            print("There will be {} green bottles hanging on the wall".format(answer))
        else:
            print("No, try again.")            
    print("There are no more green bottles hanging on the wall.")

    
    















if __name__ == '__main__':
    main()