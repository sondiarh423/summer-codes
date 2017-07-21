from turtle import *
import math

# Name your Turtle.
jane = Turtle()

# Set Up your screen and starting position.
jane.penup()
setup(800,500)
x_pos = 0
y_pos = 0
jane.setposition(x_pos, y_pos)

### Write your code below:
jane.pendown()
jane.begin_fill()
jane.fillcolor("red")
for counter in range (4):
    print (jane.forward(100))
    jane.right(90)
    jane.forward(100)
    print (counter)
jane.end_fill()


# Close window on click.
exitonclick()
