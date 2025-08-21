# ---------------------------------------------------------
# Constructing Objects And Accessing Their Attributes & Methods
# ---------------------------------------------------------

# Importing classes from the turtle module
from turtle import Turtle, Screen

# ----------------- Turtle Object -----------------
# Create a Turtle object (instance of the Turtle class)
timmy = Turtle()

# Printing the object shows its memory reference (not very useful visually)
print(timmy)

# Using METHODS (actions the object can do)
timmy.shape("turtle")   # change turtle shape to a turtle icon 🐢
timmy.color("red")      # change turtle color to red
timmy.forward(100)      # move the turtle forward 100 pixels (drawing a red line)

# ----------------- Screen Object -----------------
# Create a Screen object (the window/canvas for the turtle)
my_screen = Screen()

# Accessing an ATTRIBUTE (data belonging to the object)
print(my_screen.canvheight)   # prints the canvas height (default: 300)

# Using a METHOD of the Screen object
my_screen.exitonclick()       # keeps the window open until user clicks inside