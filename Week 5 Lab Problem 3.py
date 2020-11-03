#Jesus Navarrete
#29 October 2020

#This program will ask the user for a regular polygon by asking for the number
#of sides, the lenght of the sides, and a color to use

import turtle

sides1 = input("Number of sides ")
Lenght = input("Lenght of Sides ")
color = input("Color of polygon ")


colors = [color]

for color in colors:
    print(color)
Siege= turtle.Turtle()

def polygone (sides):
    for num in range(sides):
        Siege.right(360/side1)
        Siege.left(360/side1)
        Siege.forward(Lenght)

#'360/sides' for the turn of polygon
