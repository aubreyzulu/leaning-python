from turtle import Turtle, Screen, colormode
from random import choice, randint

tim = Turtle()
num_sides = 5
colormode(255)
# colors = ["aquamarine", "crimson", "deep pink", "goldenrod",
#           "hot pink", "indigo", "khaki", "maroon", "navy", "orchid"]


colors = ["coral", "teal", "lavender", "maroon", "gold",
          "sky blue", "orchid", "turquoise", "salmon", "slate gray"]
directions = [randint(0, 359) for _ in range(200)]


print(directions)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def draw_shape(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        tim.forward(30)
        tim.setheading(choice(directions))
        # tim.right(angle)


for num_of_shape in range(3, 11):
    tim.color(random_color())
    # tim.right(choice(directions))
    draw_shape(num_of_shape)


screen = Screen()

screen.exitonclick()
