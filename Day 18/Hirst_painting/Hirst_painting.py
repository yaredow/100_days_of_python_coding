from turtle import Turtle, Screen
import random
# import colorgram
# colors = colorgram.extract('spot.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb = (r, g, b)
#     rgb_colors.append(new_rgb)

color_list = [(141, 163, 182), (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97), (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31), (204, 67, 26), (226, 170, 199), (242, 80, 27), (16, 172, 189), (34, 176, 93), (2, 114, 63), (247, 214, 2), (114, 188, 142), (181, 95, 111), (188, 182, 211), (40, 39, 46), (157, 207, 217), (229, 173, 162), (162, 208, 181), (118, 117, 163)]
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)



def forward_dot():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
def backward_dot():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

for _ in range(10):
    forward_dot()
    backward_dot()

screen.exitonclick()


