num1 = int(input("With how many slices of pizza did you start?: "))
num2 = int(input("How many slices have you already eaten? You pig: "))
answer = num1 - num2

if answer == 0:
     print(f"You have eaten the whole damn pizza. I´m proud of you my fat little piece of shit  ")
elif answer > 0:
    print(f"You have {answer} slices left. Hurry up! The heart attack is waiting por fou. ")
else:
    print(f"Have you ordered more pizza? What´s wrong with you dude?. ")
