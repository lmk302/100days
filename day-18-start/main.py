# import turtle
# tim = turtle.Turtle()

# import turtle as t
# tim = t.Turtle()


import turtle as t




# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# for _ in range(4):
#     timmy_the_turtle.forward(200)
#     timmy_the_turtle.right(90)

# for _ in range(50):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
import random

tim = t.Turtle()
tim.colormode(255)

directions = [0, 90, 180, 270]
# colors = ["red", "blue", "orange", "yellow", "green", "black"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g ,b)
    return color
    


tim.speed(20)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(1)
# for _ in range(200):
#     tim.pensize(10)
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions)) 


screen = t.Screen()
screen.exitonclick()


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         t.forward(100)
#         t.right(angle)

# for shape_side_n in range(3, 11):
#     t.color(random.choice(colors))
#     draw_shape(shape_side_n)


