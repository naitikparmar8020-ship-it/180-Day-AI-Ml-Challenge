# from turtle import Turtle,Screen
import turtle as t
import random

tim=t.Turtle()
# print(tim)
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    # t.colormode(255)
    tim.pencolor(r,g,b)
random_color()
# tim.shape("turtle")
# colors=["#FF2A6D", "#01012B", "#05D9E8", "#01012B", "#39FF14", "#88516D"]

direction=[0,90,180,270]
tim.speed("fastest")
# now i have to define that how turtle can move randomly anywhere
# so the idea is that take step randomly from step list
# so for that what to do?
for _ in range(500):
    tim.pensize(5)
    tim.fd(30)
    random_color()
    tim.setheading(random.choice(direction))
my_screen=t.Screen()
my_screen.exitonclick()
