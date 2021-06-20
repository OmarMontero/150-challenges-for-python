import math

def cylinder_area():

    radius = float(input("Write the radius of a cylinder: "))
    depth = float(input("Write the depth of a cylinder: "))

    circle_area = math.pi * (radius ** 2)
    print(circle_area * depth)


if __name__ == '__main__':
    cylinder_area()