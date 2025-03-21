from turtle import Turtle, Screen
import random
import turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            print(turtle.pencolor())
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("Your turtle won!")
            else:
                print("Your turtle lost.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        print(turtle.xcor())
    
screen.exitonclick()