import turtle

myT = turtle.Turtle()
myT.shape("turtle")

for i in range(0,5):
    myT.circle(40)
    if(i==2):
        myT.penup()
        myT.goto(-100,-100)
        myT.pendown()
    myT.penup()    
    myT.forward(100)
    myT.pendown()
