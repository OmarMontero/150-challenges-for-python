import turtle
import random


    


def main():
    num = random.randint(0,90)
    colours = ["blue", "orange", "green", "red", "yellow", "purple" ]

    for i in range(num):
        colour = random.choice(colours)
        angle = random.randint(0, 360)
        length = random.randint(0, 60)
        turtle.color(colour)
        turtle.forward(length)
        turtle.right(angle)






if __name__ == '__main__':
    main()
