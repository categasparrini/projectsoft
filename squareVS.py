# case 2
# arbitrary rotation 
# given location is the center of the square

# center position, size and angle of rotation are variables in the code, no need to take them from the user

# case 3
# arbitrary regular polygon given the number of sides (all the other params still apply)

# case 4 
# replace the sides of the polygon with an arbitrary series of lines that scale with the size of the side


import turtle 
import math

def square(a):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    

# case 2

def rotate(angle):
    global length
    length = 150
    global x_c
    global y_c
    x_c = 75
    y_c = 75
    turtle.seth(angle)
# Distanza tra il centro e un vertice
    r = length / math.sqrt(2)

# Angolo del vertice iniziale rispetto al centro
    angle_r = math.radians(angle + 225)

# Coordinate del vertice iniziale
    x0 = x_c + r * math.cos(angle_r)
    y0 = y_c + r * math.sin(angle_r)
    turtle.teleport(x0, y0)
    square(length)

# case 3
# s is the nb of sides

#----------------------------------


def polygon(sides, length): 

    for i in range(sides):
        turtle.forward(length)
        turtle.left(360/sides)

def rotate_polygon(sides, length, angle):
    global x_c
    global y_c
    x_c = 75
    y_c = 75
    turtle.seth(angle)
# Distance between the center and a vertex
    R = length / 2*math.sin(math.radians(180/sides))

# Angle of the initial vertex with respect to the center
    angle_r = math.radians(angle + 180 + 360/(2*sides))

# Initial vertex coordinates
    x0 = x_c + R * math.cos(angle_r)
    y0 = y_c + R * math.sin(angle_r)
    turtle.teleport(x0, y0)
    

# case 4
def poly2(sides, length): 

    for i in range(sides):
        turtle.forward(length/3)
        turtle.left(90)
        turtle.forward(length/3)
        turtle.right(90)
        turtle.forward(length/3)
        turtle.right(90)
        turtle.forward(length/3)
        turtle.left(90)
        turtle.forward(length/3)
        turtle.left(360/sides)


