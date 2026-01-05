import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Welcome!")


# Turtle setup
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(10)


# Function to draw a decorative border
def draw_border():
    pen.penup()
    pen.goto(-250, 250)
    pen.pendown()
    pen.pensize(3)
    pen.color("cyan")
    for _ in range(4):
        pen.forward(500)
        pen.right(90)


# Get user input
name = screen.textinput("Your Name", "Enter your nickname:")



# Draw the decorative border

draw_border()

# Write the welcome message with a gradient effect
colors = ["red", "orange", "yellow", "green", "blue", "purple"]




if name:  # Check if a name was entered
    message = f"Welcome, {name}!"
else:
    message = "Welcome, Guest!"



pen.penup()
pen.goto(0, 0)


# Display the message letter by letter in gradient colors
for i, letter in enumerate(message):
    pen.color(colors[i % len(colors)])  # Cycle through the colors
    pen.write(letter, align="center", font=("Arial", 30, "bold"))
    pen.forward(25)  # Adjust spacing between letters



# Keep the screen open
screen.mainloop()