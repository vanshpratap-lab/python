import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Beautiful Flowers Animation")
screen.setup(width=1000, height=800)

# Create turtle for drawing
pen = turtle.Turtle()
pen.speed(6)  # Moderate speed for animation
pen.width(2)

# Function to draw a petal
def draw_petal(t, radius, angle):
    t.circle(radius, angle)
    t.left(180 - angle)
    t.circle(radius, angle)
    t.left(180 - angle)

# Function to draw rose
def draw_rose(x, y):
    pen.penup()
    pen.goto(x, y - 150)
    pen.pendown()
    pen.setheading(90)
    
    # Draw brown stem
    pen.color('#8B4513')
    pen.width(4)
    pen.forward(150)
    
    # Draw left leaf
    pen.penup()
    pen.goto(x - 10, y - 80)
    pen.pendown()
    pen.setheading(225)
    pen.color('#228B22')
    pen.width(2)
    pen.begin_fill()
    pen.circle(25, 90)
    pen.left(90)
    pen.circle(25, 90)
    pen.end_fill()
    
    # Draw right leaf
    pen.penup()
    pen.goto(x + 10, y - 100)
    pen.pendown()
    pen.setheading(315)
    pen.begin_fill()
    pen.circle(25, 90)
    pen.left(90)
    pen.circle(25, 90)
    pen.end_fill()
    
    # Draw rose petals
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.setheading(0)
    pen.color('#DC143C')
    pen.width(2)
    
    petal_size = 60
    for i in range(36):
        draw_petal(pen, petal_size, 60)
        pen.left(10)
        petal_size -= 1.5
    
    # Center of rose
    pen.penup()
    pen.goto(x, y - 8)
    pen.pendown()
    pen.color('#8B0000')
    pen.begin_fill()
    pen.circle(8)
    pen.end_fill()

# Function to draw sunflower
def draw_sunflower(x, y):
    pen.penup()
    pen.goto(x, y - 150)
    pen.pendown()
    pen.setheading(90)
    
    # Draw stem
    pen.color('#228B22')
    pen.width(4)
    pen.forward(150)
    
    # Draw sunflower petals (large yellow petals)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color('#FFD700')
    pen.width(2)
    
    for i in range(12):
        pen.setheading(i * 30)
        pen.begin_fill()
        pen.forward(50)
        pen.left(60)
        pen.forward(30)
        pen.goto(x, y)
        pen.end_fill()
    
    # Draw center (brown)
    pen.penup()
    pen.goto(x, y - 25)
    pen.pendown()
    pen.color('#8B4513')
    pen.begin_fill()
    pen.circle(25)
    pen.end_fill()
    
    # Add texture to center
    pen.color('#654321')
    for i in range(20):
        pen.penup()
        angle = i * 18
        rad = 20
        px = x + rad * math.cos(math.radians(angle))
        py = y + rad * math.sin(math.radians(angle))
        pen.goto(px, py)
        pen.pendown()
        pen.dot(4)

# Function to draw lily
def draw_lily(x, y):
    pen.penup()
    pen.goto(x, y - 150)
    pen.pendown()
    pen.setheading(90)
    
    # Draw stem
    pen.color('#228B22')
    pen.width(4)
    pen.forward(150)
    
    # Draw white lily petals
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color('white')
    pen.width(2)
    
    # Draw 6 petals
    for i in range(6):
        pen.setheading(i * 60)
        pen.begin_fill()
        pen.forward(60)
        pen.circle(20, 120)
        pen.goto(x, y)
        pen.end_fill()
    
    # Draw center (yellow stamen)
    pen.penup()
    pen.goto(x, y - 8)
    pen.pendown()
    pen.color('#FFFF00')
    pen.begin_fill()
    pen.circle(8)
    pen.end_fill()
    
    # Draw small dots for pollen
    pen.color('#FFD700')
    for i in range(6):
        pen.penup()
        angle = i * 60
        px = x + 15 * math.cos(math.radians(angle))
        py = y + 15 * math.sin(math.radians(angle))
        pen.goto(px, py)
        pen.pendown()
        pen.dot(5)

# Function to write message
def write_message():
    text_pen = turtle.Turtle()
    text_pen.hideturtle()
    text_pen.penup()
    text_pen.goto(0, -320)
    text_pen.color('#FFD700')
    text_pen.write("For Love of My Life", align="center", 
                   font=("Arial", 28, "bold"))

# Main execution
pen.hideturtle()

# Draw three flowers
draw_rose(-250, 50)
draw_sunflower(0, 50)
draw_lily(250, 50)

# Write message
write_message()

# Keep window open
screen.mainloop()