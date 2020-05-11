# ****** Turtle Race ******

# *******************************

# ****** Importing Modules ******
import random
import time
import turtle

# ****** Creating our turtle object ******
tur = turtle.Turtle()

# ****** Title ******
tur.screen.title("Welcome to the turtle race!!!")

# ****** Background Color ******
tur.getscreen().bgcolor('green')

tur.hideturtle()
tur.penup()
tur.setposition(-10, 290)
tur.pendown()

# ****** Writing title on screen ******
style = ('Verdana', 30, "bold")
tur.write('Welcome to the turtle race!!!', font=style, align='center')

tur.penup()
tur.goto((300, 250))
tur.pendown()
tur.right(90)

# ****** Creating the finish line ******
tur.speed(20)

for _ in range(2):
    for i in range(16):
        if i%2:
            tur.color("white", "white")
        else:
            tur.color("black", "black")
        tur.begin_fill()
        for _ in range(4):
            tur.forward(25)
            tur.right(90)
        tur.end_fill()
        tur.penup()
        tur.forward(25)
        tur.pendown()
    tur.penup()
    tur.left(180)
    tur.pendown()

# ****** Making our turtles ******

tur1 = turtle.Turtle()
tur1.hideturtle()

tur2 = turtle.Turtle()
tur2.hideturtle()

tur3 = turtle.Turtle()
tur3.hideturtle()

tur4 = turtle.Turtle()
tur4.hideturtle()

tur5 = turtle.Turtle()
tur5.hideturtle()

turtles = [tur1, tur2, tur3, tur4, tur5]
colors = ['Red', 'Cyan', 'Blue', 'Yellow', 'Orange']
y_positions = [150, 100, 50, 0, -50]

for tur, color, y_pos in zip(turtles, colors, y_positions):
    tur.showturtle()
    tur.shape("turtle")
    tur.color(color)
    tur.penup()
    tur.goto((-300, y_pos))
    tur.pendown()

# ****** Waiting for 1 second before the race starts ******
time.sleep(1)

# ****** Logic for stopping when turtle reaches the finish line ******
status = 'not finished'
winner = 'no one'
finish_position = (260, 200)

while True:

    # Checking if any turtle has reached the finish position
    for tur in turtles:
        x, y = tur.position()
        if (x, y) >= finish_position:
            winner = turtles.index(tur)
            status = 'finished'

    # Stoping the race if any turtle has reached the finish position
    if status == 'finished':
        break

    # Moving each turtle
    tur1.forward(random.randint(1, 5))
    tur2.forward(random.randint(1, 5))
    tur3.forward(random.randint(1, 5))
    tur4.forward(random.randint(1, 5))
    tur5.forward(random.randint(1, 5))

# ****** Announcing the winner ******
for tur in turtles:
    tur.pendown()

winner_name = turtle.Turtle()
winner_name.penup()
winner_name.hideturtle()
winner_name.setposition(-5, -220)
winner_name.pendown()

style = ('Verdana', 30, "bold")
winner_name.write(f"Winner of the race is {colors[winner]} turtle!!!", font=style, align='center')

# ****** Our event loop ******
turtle.mainloop()

# *******************************
