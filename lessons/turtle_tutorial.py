from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(250)
i: int = 0
leo.penup()
leo.goto(-150, -50)
leo.pendown()
# leo.color(99, 204, 250)
leo.begin_fill()
# code for shape to be filled 
leo.speed(50)
leo.hideturtle()
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()    
done()
