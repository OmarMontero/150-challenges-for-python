import turtle

def main():
    for x in range(10):   
        for i in range(8):
            turtle.forward(50)
            turtle.right(360/8)
        turtle.right(36)

    turtle.exitonclick()

if __name__ == '__main__':
    main()