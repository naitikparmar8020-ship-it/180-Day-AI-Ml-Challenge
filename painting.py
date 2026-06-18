import colorgram
import turtle as t
import random
# rgb_color=[]
# colors=colorgram.extract(r'D:\100day python\day18\hirst.jpg',30)

# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_color.append(new_color)

# print(rgb_color)

color_list=[(237, 247, 252), 
            (226, 147, 98), (28, 102, 177), (161, 56, 90), (148, 79, 51), 
            (225, 61, 96), (113, 174, 215), (244, 227, 95), (173, 20, 41), 
            (233, 79, 51), (224, 126, 156), (118, 184, 130), (11, 172, 207), 
            (165, 151, 25), (13, 58, 148), (83, 37, 23), (128, 37, 27), (37, 129, 78), 
(42, 192, 160), (14, 39, 92), (129, 238, 190), (244, 162, 151), (235, 162, 181), 
(100, 101, 186), (127, 214, 239), (66, 77, 38), (74, 31, 46)]

tim=t.Turtle()
# print(tim)
t.colormode(255)
x_cor=int(-250)
y_cor=int(-250)
tim.hideturtle()
tim.teleport(x_cor,y_cor)
tim.speed("fastest")
def single_row():
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)

for row in range(1,11): #(-250,-250)
    single_row()
    x_cor += 0
    y_cor += 50
    tim.teleport(x_cor,y_cor)
    
my_screen=t.Screen()
my_screen.exitonclick()