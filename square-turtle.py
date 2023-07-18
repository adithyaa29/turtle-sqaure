import turtle
t = turtle.Turtle()
#t.pencolor("blue") #Set pen colour to blue(Black is the default colour)
def square(t,length):
    for i in range(4):
        t.forward(length) 
        t.left(90)
square(t,100)
turtle.done()