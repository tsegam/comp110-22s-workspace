"""Shape designs using Turtle library. My ultimate output is a bunch of shapes with interesting combination, quote nice abstract!"""
from turtle import Turtle, done, colormode 
__author__ = "730439223"
__name__ == "__main__"


def draw_square(a_square: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_square.penup()
    a_square.goto(x, y) 
    a_square.setheading(0.0)
    a_square.pendown()
    i: int = 0
    while i < 4:
        a_square.forward(width)
        a_square.right(90)
        i = i + 1


def draw_triangle(leo: Turtle, x: float, y: float, width: float, color: int) -> None: 
    """Draw a triangle, takes x and y as arguement for start position and width and color."""
    colormode(color)
    i: int = 0
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    # leo.color(99, 204, 250)
    leo.begin_fill()
    # code for shape to be filled 
    leo.speed(50)
    leo.hideturtle()
    while (i < 3):
        leo.forward(300)
        leo.left(width)
        i = i + 1
    leo.end_fill()    
   

def draw_triangle_wider(leo: Turtle, x: float, y: float, width: float, color: int) -> None: 
    """Draw a wide triangle, takes x and y as arguement for start position and width and color."""
    colormode(color)
    i: int = 0
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.fillcolor("#33cc8c")  # Fill color of greenish paint.
    leo.pencolor("#43cc8c")  # pen color as per requirement.
    leo.begin_fill()
    # code for shape to be filled 
    leo.speed(50)
    leo.hideturtle()
    while (i < 3):
        leo.forward(350)
        leo.left(width)
        i = i + 1
    leo.end_fill() 


def draw_rectangle(a_rect: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_rect.penup()
    a_rect.goto(x, y) 
    a_rect.setheading(0.0)
    a_rect.pendown()
    # draw top
    a_rect.forward(width)
    # draw right
    a_rect.right(90)
    a_rect.forward(height)
    # draw bottom
    a_rect.right(90)
    a_rect.forward(width)
    # draw left
    a_rect.right(90)
    a_rect.forward(height)
    

def main() -> None:  # Main doesn't take any parametters runs 6 functions. Created above.
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    
    draw_square(ertle, -50, 50, 100)
    draw_triangle(ertle, -150, 50, 120, 250)
    draw_square(ertle, 100, 50, 100)
    draw_square(ertle, -200, 50, 100)
    draw_triangle_wider(ertle, -10, 25, 500, 250)
    draw_rectangle(ertle, -100, -50, 200, 100)
    done()


if (__name__ == "__main__"):
    main()