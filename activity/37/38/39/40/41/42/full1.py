import turtle

# creating canvas
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(4):
	board.forward(100)
	board.left(90)
	i = i+1



import turtle

turtle.Screen().bgcolor("Orange")
board = turtle.Turtle()
 
# first triangle for star
board.forward(100) # draw base
 
board.left(120)
board.forward(100)
 
board.left(120)
board.forward(100)
 
board.penup()
board.right(150)
board.forward(50)
 
# second triangle for star
board.pendown()
board.right(90)
board.forward(100)
 
board.right(120)
board.forward(100)
 
board.right(120)
board.forward(100)
 
turtle.done()







# import turtle
import turtle

# defining colors
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']

# setup turtle pen
t= turtle.Pen()

# changes the speed of the turtle
t.speed(10)

# changes the background color
turtle.bgcolor("black")

# make spiral_web
for x in range(200):
	t.pencolor(colors[x%6]) # setting color
	t.width(x/100 + 1) # setting width
	t.forward(x) # moving forward
	t.left(59) # moving left

turtle.done()
t.speed(10)

turtle.bgcolor("black") # changes the background color

# make spiral_web
for x in range(200):
	t.pencolor(colors[x%6]) # setting color
	t.width(x/100 + 1) # setting width
	t.forward(x) # moving forward
	t.left(59) # moving left

turtle.done()
