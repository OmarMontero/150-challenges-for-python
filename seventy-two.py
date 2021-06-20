

def main():
    
    subjects = ["maths", "biology", "music", "history", "information technology", "geography"]
    print(subjects)
    subject = input("which of these subjects you don´t like?: ")
    
    for i in subjects:
        if i == subject:
            subjects.remove(i)
    
    print(subjects)







if __name__ == '__main__':
    main()