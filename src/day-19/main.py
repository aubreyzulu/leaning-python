from turtle import Turtle, Screen


screen = Screen()

screen.setup(500, 400)

user_bet = screen.textinput(
    "Make your bet", "Which turtle will win the race? Enter a colour: ")

tim = Turtle()
tim.goto(y=-100, x=230)
screen.exitonclick()
