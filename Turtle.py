import turtle as t

tim = t.Turtle()


def Draw_shape(num_sides) :
    angel = 360 // num_sides
    for _ in range(num_sides) :
        tim.forward(100)
        tim.right(angel)
tim.color("blue")
for num in range(3,11):
    Draw_shape(num)