
"""
106 Create a new file called “Names.txt”. Add five names to the
document, which are stored on separate lines. Once you have
run the program, look in the location where your program is
stored and check that the file has been created properly.
"""
def main():
    file = open("names.txt", "w")
    name = ["Omar", "Ana", "Marta", "Elena", "Anita"]
    for i in name:
        file.write(str(i) + "\n")

    file.close()





if __name__ == '__main__':
    main()