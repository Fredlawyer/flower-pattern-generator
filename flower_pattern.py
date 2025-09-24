import turtle
import random

screen = turtle.Screen() # drawing window
screen.bgcolor("pink")
screen.title("Flower")
swidth = 800
sheight = 600
screen.setup(width=swidth, height=sheight)

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

colors = ['purple', 'salmon', 'purple', 'white', 'violet']

def flower(x=0, y=0, rotation=0, color='red'):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.fillcolor(color)
    t.pencolor("purple") # outline
    
    t.right(rotation) #for the random rotation
    t.begin_fill()
    for _ in range(6): #draws flower with 6 petals
        t.circle(20, 60)
        t.left(120)
        t.circle(20, 60) #to form full petal
        t.left(60) 
    t.end_fill()
    t.left(rotation) #rotates back to original

def pattern(x, y, x_end, y_end, color_index=0, x_step=60, y_step=60):
    if y < y_end:  # base case: stop if bottom is reached
        return
    if x > x_end:  # move to the next row, resets x
        pattern(-x_end, y - y_step, x_end, y_end, color_index, x_step, y_step)
        return
    
    rotation_angle = random.randint(0, 360) #so they are rotated randonmly
    current_color = colors[color_index % len(colors)] #cycles through color list, this ensures that result stays within valid index range
    flower(x=x, y=y, rotation=rotation_angle, color=current_color)
    
    #moves to the next column (x + step)
    pattern(x + x_step, y, x_end, y_end, color_index + 1, x_step, y_step)

#start at the top-left corner
pattern(-swidth//2, sheight//2, swidth//2, -sheight//2, color_index=0, x_step=60, y_step=60)

t.hideturtle()

canvas = screen.getcanvas()
canvas.postscript(file="myflower.eps")
screen.exitonclick()