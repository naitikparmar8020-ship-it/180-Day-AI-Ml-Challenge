from turtle import Turtle,Screen
import random
tim=Turtle()
print(tim)

# draw a triangle, square , pentagon , hexagone , heptagon , octagon , 
# nonagon and decagon
colors=["#FF2A6D", "#01012B", "#05D9E8", "#01012B", "#39FF14", "#88516D"]
def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.fd(100)
        tim.right(angle)
for shape in range (3,11):
    tim.color(random.choice(colors))
    draw_shape(shape)
my_screen=Screen()
my_screen.exitonclick()
