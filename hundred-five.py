"""
105 Write a new file called “Numbers.txt”. Add five numbers to the document which are stored on the same line and only separated by a comma.
Once you have run the program, look in the location where your program is stored and you should see that the file has been created.
The easiest way to view the contents of the new text file on a Windows system is to read it using Notepad.

"""
def main():
    file = open("numbers.txt", "w")

    for i in range(1, 6):
        file.write(str(i) + ",")

    file.close()





if __name__ == '__main__':
    main()