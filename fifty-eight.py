import random

def main():
    print("*" * 50)
    print("Wellcome to the math quiz!")

    score = 0
 
    for i in range(5):
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        answer = int(input(f" {num1} + {num2}=  "))
        result = num1 + num2       
        if answer == result:
            score = score + 1

        print("You got {} correct answers.".format(score))





if __name__ == '__main__':
    main()