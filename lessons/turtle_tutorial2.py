"""TODO: Describe your scene program."""
from turtle import Turtle, done 
__author__ = "730439223"
__name__ == "__main__"


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
    done()


# TODO: Define the procedures for other components in your scene here.

# TODO: Use the __name__ is "__main__" idiom shown in 


def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    draw_square(ertle, -5, 5, 10)
    draw_square(ertle, -10, 10, 20)
    draw_square(ertle, -15, 15, 30)
    draw_square(ertle, -20, 20, 40)
    done()
    # Challenge: Try rewriting those four repeated calls in a loop
    # and using arithmetic expressions to calculate each of the arguments
    # based on your counter variable's value rather than hard coded int
    # literals. For example, the first argument could be: (i + 1) * -5


if (__name__ == "__main__"):
    main()