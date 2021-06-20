import turtle
import random


def main():
    colours = ["blue", "orange", "green", "red", "yellow", "purple" ]
    


    for i in range(6):
        colour = random.choice(colours)
        turtle.color(colour)
        turtle.forward(50)
        turtle.right(360/6)



if __name__ == '__main__':
    main()
