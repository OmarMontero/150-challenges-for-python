import turtle
import random


def oldtimes():

    for i in range(4):
        turtle.color("red")
        turtle.forward(10)
        turtle.right(90)
        

    turtle.penup()
    turtle.forward(20)
    turtle.pendown()

    for i in range(4):
        turtle.color("blue")
        turtle.forward(10)
        turtle.right(90)
        

    turtle.penup()
    turtle.forward(20)
    turtle.pendown()

    for i in range(4):
        turtle.color("black")
        turtle.forward(10)
        turtle.right(90)

def newtimes():
    colours = ["black", "blue", "red"]

    for i in range(3):
        colour = colours.index[i]
        turtle.color(colour)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()    

        for i in range(4):
            turtle.color("black")
            turtle.forward(10)
            turtle.right(90)







if __name__ == '__main__':
    #oldtimes()
    newtimes()
    


