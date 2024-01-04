# import colorgram
#
#
# colors = colorgram.extract('image.jpg', 20)
# list_colors = []
# for i in range(len(colors)):
#     # list_colors.append(colors[i].rgb)
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.r
#     tup = (r, g, b)
#     list_colors.append(tup)
from turtle import Turtle, Screen
import turtle as turtu
import random
color_list_new = [(253, 251, 253), (253, 248, 253), (235, 252, 235), (198, 13, 198), (248, 236, 248), (40, 76, 40), (244, 247, 244), (39, 216, 39), (238, 227, 238), (227, 159, 227), (29, 40, 29), (212, 76, 212), (17, 153, 17), (241, 36, 241), (195, 16, 195), (223, 21, 223), (68, 10, 68), (61, 15, 61), (223, 141, 223), (11, 97, 11)]
turtu.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.hideturtle()
tim.speed("fastest")
# def random_color():
#
#     tup = color_list_new(random.choice())
#     return tup
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1,number_of_dots):
    tim.dot(20, random.choice(color_list_new))
    tim.forward(50)
    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()



