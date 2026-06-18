import turtle as t
import random
tim=t.Turtle()

print(tim)

# tim.circle(100)

# def create_spirograph():
#     # angle=360/radius
#     for _ in range(shape):
#         tim.left(10)
#         tim.speed("fast")

t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
def draw_spirogrpah(gap):

    for _ in range(int(360/gap)):
        tim.pensize(2)
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap)
        tim.speed("fastest")
draw_spirogrpah(5)
my_screen=t.Screen()
my_screen.exitonclick()