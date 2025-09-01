import turtle
import math

# Setup turtle
t = turtle.Turtle()
t.speed(20)                 # fast drawing
t.shape("turtle")           # turtle shape cursor
t.getscreen().bgcolor("#ffcaaa")  # background color

# Circle radii
outer_radius = 300
inner_radius = 250

# Function to draw repeated petal-like patterns using circles
def petals(num, length):
    t.pu()
    t.home()                # reset to center
    t.pd()
    t.setheading(0)
    angle = 360 / num       # divide full circle into equal petals
    theta = 0
    t.begin_fill()
    for i in range(num):
        t.setheading(theta)
        t.circle(length)    # draw circular arc
        theta += angle
    t.end_fill()

# ---------------- DRAWING STARTS ---------------- #


# OUTERMOST DARK GREEN CIRCLE
t.color("#1a4e1b", "#1a4e1b")
t.begin_fill()
t.pu()
t.goto(outer_radius, 0)     # move to right edge
t.left(90)
t.pd()
t.circle(outer_radius)      # draw big circle
t.end_fill()

# INNER ORANGE CIRCLE
t.goto(inner_radius, 0)     # move to new radius
t.color("white", "#ff8800")
t.begin_fill()
t.circle(inner_radius)
t.end_fill()

#first SQUARE (ROTATED)
colors = ['red', 'orange', 'yellow', 'white']
c = inner_radius * math.sqrt(2)  # diagonal length (outermost square)

t.penup()
t.goto(0, 0)
t.setheading(0)
t.forward(c/2)
t.left(90)
t.forward(c/2)
t.left(90)
for idx, color in enumerate(colors):
    offset = idx * (c * 0.04)  # bigger squares, thinner lines
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.forward((c/2) - offset)
    t.left(90)
    t.forward((c/2) - offset)
    t.left(90)
    t.pendown()
    t.color(color)
    t.width(2)  # thinner lines
    t.begin_fill()
    for _ in range(4):
        t.forward(c - 2*offset)
        t.left(90)
    t.end_fill()
    t.width(1)

# second SQUARE SECTION
y = inner_radius/2 + 60
# Draw concentric squares on the red square section
y = inner_radius/2 + 60
# Second square section at 45°
colors = ['red', 'orange', 'yellow', 'white']
t.penup()
t.goto(0, 0)
t.setheading(30)
t.forward(c/2)
t.left(90)
t.forward(c/2)
t.left(90)
for idx, color in enumerate(colors):
    offset = idx * (c * 0.04)
    t.penup()
    t.goto(0, 0)
    t.setheading(30)
    t.forward((c/2) - offset)
    t.left(90)
    t.forward((c/2) - offset)
    t.left(90)
    t.pendown()
    t.color(color)
    t.width(2)
    t.begin_fill()
    for _ in range(4):
        t.forward(c - 2*offset)
        t.left(90)
    t.end_fill()
    t.width(1)

# third SQUARE SECTION
y = inner_radius/2 + 60
# Draw concentric squares on the red square section

# Third square section at 90°
colors = ['red', 'orange', 'yellow', 'white']
t.penup()
t.goto(0, 0)
t.setheading(60)
t.forward(c/2)
t.left(90)
t.forward(c/2)
t.left(90)
for idx, color in enumerate(colors):
    offset = idx * (c * 0.04)
    t.penup()
    t.goto(0, 0)
    t.setheading(60)
    t.forward((c/2) - offset)
    t.left(90)
    t.forward((c/2) - offset)
    t.left(90)
    t.pendown()
    t.color(color)
    t.width(2)
    t.begin_fill()
    for _ in range(4):
        t.forward(c - 2*offset)
        t.left(90)
    t.end_fill()
    t.width(1)

# PURPLE CIRCLE BETWEEN BROWN PETALS AND YELLOW SQUARE
purple_radius = inner_radius - 76  # Adjust as needed to fit between brown and yellow
t.pu()
t.goto(purple_radius, 0)
t.setheading(90)
t.pd()
t.color("purple", "purple")
t.begin_fill()
t.circle(purple_radius)
t.end_fill()    

# INNER BROWN PETALS
t.color("brown")
petals(6, inner_radius-150)

# RED THICK BORDER NEAR EDGE
t.color("red")
t.pu()
z = outer_radius + 70  # Make the border closer to the outermost edge
t.goto(z, 0)
t.setheading(90)
t.width(130)                 # thicker border
t.pd()
t.circle(z)
t.width(5)

# YELLOW PETALS AROUND
t.setheading(90)
t.color("yellow")
n = 6  # no.of petals
petals(n, inner_radius)


# LIGHT GREEN INNER CIRCLE RING
t.color("white", "white")
small_radius = y/2 + 5  # Increase radius by 20 units
t.pu()
t.setpos(small_radius,0)
t.setheading(90)
t.pd()
t.begin_fill()
t.circle(small_radius)
t.end_fill()

# Add img.gif inside the light green inner circle ring
screen = t.getscreen()
try:
    screen.addshape("img.gif")
except turtle.TurtleGraphicsError:
    pass  # shape may already be registered
t.pu()
t.goto(0, 0)
t.shape("img.gif")
t.shapesize(small_radius/200)
t.stamp()
t.shape("turtle")  # Reset shape to avoid accidental stamping elsewhere

# Draw red ring in front of the gif
red_ring_radius = small_radius
# Draw only the ring, not filled
t.pu()
t.goto(red_ring_radius, 0)
t.setheading(90)
t.pd()
t.color("red")
t.width(20)
t.circle(red_ring_radius)
t.width(1)

# Draw green ring above OUTERMOST DARK GREEN CIRCLE, in front of yellow petals
green_ring_radius = outer_radius-25
t.pu()
t.goto(green_ring_radius, 0)
t.setheading(90)
t.pd()
t.color("green")
t.width(50)
t.circle(green_ring_radius)
t.width(1)

    # End drawing
turtle.done()
