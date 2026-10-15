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

def rotate():
    global side
    side = 150
    global x_c
    global y_c
    x_c = 20
    y_c = 30
    global angle
    angle = 60
    turtle.seth(angle)
# Distanza tra il centro e un vertice
    r = side / math.sqrt(2)

# Angolo del vertice iniziale rispetto al centro
    angle_r = math.radians(60 + 225)

# Coordinate del vertice iniziale
    x0 = x_c + r * math.cos(angle_r)
    y0 = y_c + r * math.sin(angle_r)
    turtle.teleport(x0, y0)
    square(side)




