import turtle as t
tim=t.Turtle()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def anti_clockwise():
    tim.left(10)
def clockwise():
    tim.right(10)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
my_screen=t.Screen()
my_screen.listen()
my_screen.onkey(key="w",fun=move_forward)
my_screen.onkey(key="s",fun=move_backward)
my_screen.onkey(key="a",fun=anti_clockwise)
my_screen.onkey(key="d",fun=clockwise)
my_screen.onkey(key="c",fun=clear_drawing)
my_screen.exitonclick()