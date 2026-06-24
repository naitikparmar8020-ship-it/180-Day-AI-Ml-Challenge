from turtle import Turtle,Screen
import random
still_running=True
my_screen=Screen()
my_screen.setup(width=500,height=500)
bet=my_screen.textinput(title="make your bet",prompt="which colour of turtle will win?")

colour=["red","yellow","purple","green","blue"]
all_turtle=[]
# move_forward=[10,20]

y_pos=[-100,-50,0,50,100]
for turtle_index in range(0,5):
        
    tim=Turtle(shape="turtle")
    tim.color(colour[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y_pos[turtle_index])
    all_turtle.append(tim)
if bet:
    still_running=True

while still_running:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            still_running=False
            wining_tur=turtle.pencolor()
            if wining_tur==bet:
                print(f"congratulation! your {wining_tur} turtle is winner")
            else:
                print(f"Bad Luck! {wining_tur} turtle is winner")
        
        rand_dis=random.randint(0,10)
        turtle.forward(rand_dis)
        

my_screen.exitonclick()
