# import colorgram
# rgbColor = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgbColor.append((r, g, b))
#
# print(rgbColor)
from turtle import Turtle, colormode, Screen
from random import choice

color_list = [(108, 110, 126), (209, 155, 98), (140, 141, 152), (186, 62, 31), (225, 213, 111), (233, 214, 224),
              (207, 148, 178), (102, 110, 172), (177, 157, 44), (222, 230, 223), (28, 27, 68), (29, 46, 28),
              (38, 41, 19), (194, 20, 7), (225, 169, 197), (209, 88, 63), (44, 46, 103), (234, 173, 160), (129, 80, 90),
              (157, 167, 159), (182, 184, 214), (84, 97, 85), (208, 80, 105), (183, 15, 22), (47, 28, 48), (70, 71, 42),
              (223, 205, 26), (52, 71, 54)]
colormode(255)

tim = Turtle()
screen = Screen()

screen.screensize(1000, 1000)
screen.setworldcoordinates(-30, -30, 500, 500)

tim.speed(10)


def myTimmy(h):
    tim.penup()
    tim.hideturtle()
    for i in range(h):
        tim.setx(0)
        tim.sety(i * 50)
        for j in range(h):
            tim.color(choice(color_list))
            tim.dot(20)
            tim.forward(50)

    screen.exitonclick()


myTimmy(10)
