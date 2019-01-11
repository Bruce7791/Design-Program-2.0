# My design program that uses Turtle graphics to create various designs and art. 
# A 2nd design program using Turtle graphics as a challenge to see if I can make a 2nd one.
# OOP style pseudoclasses and static methods.

# ==============================================================================================================================
# Modules

import turtle
from turtle import Turtle
from turtle import *
import random
from random import shuffle
import math
import numpy as np

# ==============================================================================================================================
# Classes

class Spiral_Square:

    def __init__(self):
        pass

    @staticmethod
    def spiralSquare1():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Triangle Attack")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            ninja.pencolor(colors[x % 6])
            z = math.cos(x)
            a = math.sin(x)
            ninja.width(x / 5000 + 1)
            ninja.forward(x*z*a*a)
            ninja.right(120)
            ninja.forward(x*z*a*a)
        screen.update()
            
    @staticmethod
    def spiralSquare2():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Space Flower")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['blue', 'green']
        colors2 = ['purple', 'pink', 'gray', 'violet']
        for x in range(5000):
            z = 1.59
            a = math.sin(z)
            ninja.pencolor(colors2[x % 4])
            ninja.width(x / 600 + 1)
            ninja.circle(20)
            ninja.forward(x*z*a)
            ninja.pencolor(colors[x % 2])
            ninja.circle(540)
            ninja.right(157)
            ninja.right(751)
        screen.update()
            
    @staticmethod
    def spiralSquare3():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Dimensions of Lines")
        t=Turtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'hot pink', 'white']
        for x in range(5000):
            z = math.cos(x)
            a = math.sin(x)
            ninja.circle(10*z)
            ninja.circle(20*a)
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 150 + 1)
            ninja.forward(x*z)
            ninja.right(630)
            ninja.forward(x*a)
            ninja.left(630)
            ninja.forward(x*z)
            ninja.right(630)
        screen.update()
                 
    @staticmethod
    def spiralSquare4():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("The Brilliance from Within")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'blue', 'orange', 'yellow']
        colors2 = ['ForestGreen']
        colors3 = ['blue', 'red']
        for x in range(5000):
            a = math.atan(x)
            ninja.pencolor(colors[x % 4])
            ninja.width(x / 500 + 1)
            ninja.forward(x*a)
            ninja.right(491)
            ninja.backward(a)
            ninja.left(350)
            ninja.right(35)
            ninja.pencolor(colors2[x % 1])
            ninja.circle(540)
            ninja.backward(a)
            ninja.pencolor(colors3[x % 2])
            ninja.circle(50)
            ninja.right(a)
        screen.update()

    @staticmethod
    def spiralSquare5():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Trump Death Spirals")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('gray')
        num = random.randrange(1, 4)
        print("Three different Trump Death Spirals")
        print("This is Trump Death Spiral number", num)
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        a = math.cos(144)
        b = math.sin(220)
        c = math.tan(144)
        d = math.tan(220)
        colors = ['red','white','Blue']
        if num == 1:
            for i in range(5000):
                ninja.speed(0)
                ninja.up()
                ninja.write("Trump")
                ninja.forward(i * 0.5 )
                ninja.right(144 * a+b)
                ninja.forward(220 * b+a)
                ninja.pencolor(colors[i % 3])
        elif num == 2:
            for i in range(5000):
                ninja.speed(0)
                ninja.up()
                ninja.write("Trump")
                ninja.forward(i * 0.5 )
                ninja.right(220 * a+b)
                ninja.forward(220 * b+a)
                ninja.pencolor(colors[i % 3])
        elif num == 3:
            for i in range(5000):
                ninja.speed(0)
                ninja.up()
                ninja.write("Trump")
                ninja.forward(i * 0.5 )
                ninja.right(144 * c+d)
                ninja.forward(144 * d+c)
                ninja.pencolor(colors[i % 3])
            screen.update()

    @staticmethod
    def spiralSquare6():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Higgs Boson")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['OrangeRed3', 'yellow', 'forestgreen']
        colors2 = ['blue', 'red', 'green', 'violet']
        colors3 = ['pink', 'purple']
        colors4 = ['yellow', 'BlueViolet', 'DarkMagenta']
        for x in range(5000):
            z = 0.59
            a = math.atan(x)
            b = math.sin(z)
            ninja.penup()
            ninja.pencolor(colors[x % 3])
            ninja.width(x / 350 + 1)
            ninja.forward(x*b)
            ninja.right(679)
            ninja.backward(x*a)
            ninja.right(625)
            ninja.forward(x)
            ninja.right(691)
            ninja.forward(x)
            ninja.right(2100)
            ninja.pendown()
            ninja.dot(30)
            ninja.pencolor(colors3[x % 2])
            ninja.circle(5)
            ninja.right(a)
            ninja.pencolor(colors2[x % 4])
            ninja.width(x / 350 + 1)
            ninja.circle(12)
            ninja.forward(x)
            ninja.left(a)
            ninja.circle(12)
            ninja.forward(x)
            ninja.right(a)
            ninja.pencolor(colors4[x % 3])
            ninja.dot(12)
        screen.update()
            
    @staticmethod
    def spiralSquare7():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Riding the wave of the Explosion")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'yellow']
        colors2 = ['ForestGreen', 'purple']
        colors3 = ['DeepPink', 'blue']
        colors4 = ['yellow', 'MediumBlue']
        for x in range(5000):
            z = 0.59
            a = math.atan(x)
            b = math.sin(z)
            ninja.pencolor(colors4[x % 2])
            ninja.width(x / 500 + 1)
            ninja.forward(x+100)
            ninja.right(30)
            ninja.forward(20)
            ninja.left(a*b*260.5)
            ninja.forward(50)
            ninja.right(130)
            ninja.pencolor(colors[x % 4])
            ninja.dot(10)
            ninja.pencolor(colors4[x % 2])
            ninja.penup()
            ninja.setposition(0, 0)
            ninja.pendown()
            ninja.right(2)
            ninja.circle(150)
            ninja.pencolor(colors3[x % 2])
            ninja.circle(185*b)
            ninja.pencolor(colors2[x % 2])
            ninja.circle(150*a)
        screen.update()

    @staticmethod
    def spiralSquare8():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("The Emergent Phenomena")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['yellow', 'purple', 'blue', 'green', 'orange', 'red']
        c = 0.59
        d = math.atan(c)
        for x in range(10000):
            a = [91, 191, 891]
            b = a[x%3]
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 2000 + 1)
            ninja.forward(x*d*d*d)
            ninja.right(b+b)
            ninja.dot(20)
            ninja.circle(20)
        screen.update()
            
    @staticmethod
    def spiralSquare9():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Tropical Christmas")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('gray')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        for x in range(5000):
            a = [91.3, 91.4, 91.5]
            b = a[x%3]
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(91)
            ninja.right(b*b)
        screen.update()

    @staticmethod
    def spiralSquare10():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("The Eye of Chaos")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('gray')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        colors = [ 'red', 'yellow', 'blue', 'brown', 'green', 'black']
        for x in range(5000):
            a = [91.2, 91.3, 91.4]
            b = a[x%3]
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 1000 + 1)
            ninja.forward(x)
            ninja.right(91)
            ninja.right(b*b*b*b*b)
            ninja.dot(10)
        screen.update()
            
    @staticmethod
    def spiralSquare11():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("46 in One")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('black')
        print("46 different designs with one chosen by random each time the program is started.")
        num = random.randrange(1, 46)
        print("This is design number", num)
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        ninja2 = turtle.Turtle()
        ninja2.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        if num == 1:
            for x in range(5000):
                a = [30.3, 30.4, 30.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 2:
            for x in range(5000):
                a = [30.03, 30.04, 30.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 3:
            for x in range(5000):
                a = [30.03, 30.04, 30.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b+b)
        elif num == 4:
            for x in range(5000):
                a = [30.003, 30.004, 30.005]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b+b)
        elif num == 5:
            for x in range(5000):
                a = [30.03, 30.04, 30.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b+b+b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b+b+b+b+b)
        elif num == 6:
            for x in range(5000):
                a = [30.03, 30.04, 30.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b+b+b)
        elif num == 7:
            for x in range(5000):
                a = [30.003, 30.004, 30.005]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b+b+b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b+b+b+b+b)
        elif num == 8:
            for x in range(5000):
                a = [30.03, 30.04, 30.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b*b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 9:
            for x in range(5000):
                a = [30.3, 30.4, 30.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b*b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b+b)
        elif num == 10:
            for x in range(5000):
                a = [30.3, 30.4, 30.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b*b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b*b)
        elif num == 11:
            for x in range(5000):
                a = [30.03, 30.04, 30.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b*b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b*b)
        elif num == 12:
            for x in range(5000):
                a = [30.003, 30.004, 30.005]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b*b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b*b)
        elif num == 13:
            for x in range(5000):
                a = [30.3, 30.04, 30.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b+b)
        elif num == 14:
            for x in range(5000):
                a = [60.0003, 60.0004, 60.0005]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 15:
            for x in range(5000):
                a = [60.003, 60.004, 60.005]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 16:
            for x in range(5000):
                a = [60.03, 60.04, 60.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 17:
            for x in range(5000):
                a = [60.3, 60.4, 60.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 18:
            for x in range(5000):
                a = [60.3, 60.4, 60.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 19:
            for x in range(5000):
                a = [60.3, 60.4, 60.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b+b)
        elif num == 20:
            for x in range(5000):
                a = [60.3, 60.4, 60.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b+b+b)
        elif num == 21:
            for x in range(5000):
                a = [60.03, 60.04, 60.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b+b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b+b+b+b)
        elif num == 22:
            for x in range(5000):
                a = [60.3, 60.4, 60.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b+b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b+b+b+b)
        elif num == 23:
            for x in range(5000):
                a = [60.03, 60.04, 60.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b*b*b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b*b*b)
        elif num == 24:
            for x in range(5000):
                a = [90.3, 90.4, 90.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 25:
            for x in range(5000):
                a = [90.03, 90.04, 90.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 26:
            for x in range(5000):
                a = [90.3, 90.4, 90.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b*b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b*b)
        elif num == 27:
            for x in range(5000):
                a = [120.3, 120.4, 120.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 28:
            for x in range(5000):
                a = [140.3, 140.4, 140.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 29:
            for x in range(5000):
                a = [140.03, 140.04, 140.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 30:
            for x in range(5000):
                a = [140.003, 140.004, 140.005]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 31:
            for x in range(5000):
                a = [140.3, 140.4, 140.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b*b*b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b*b*b)
        elif num == 32:
            for x in range(5000):
                a = [150.03, 150.04, 150.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 33:
            for x in range(5000):
                a = [150.3, 150.4, 150.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 34:
            for x in range(5000):
                a = [150.3, 150.4, 150.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 35:
            for x in range(5000):
                a = [150.3, 150.4, 150.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b*b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b*b)
        elif num == 36:
            for x in range(5000):
                a = [160.3, 160.4, 160.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b+b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 37:
            for x in range(5000):
                a = [160.3, 160.4, 160.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b*b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b*b)
        elif num == 38:
            for x in range(5000):
                a = [170.3, 170.4, 170.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 39:
            for x in range(5000):
                a = [170.03, 170.04, 170.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 40:
            for x in range(5000):
                a = [170.003, 170.004, 170.005]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 41:
            for x in range(5000):
                a = [210.3, 210.4, 210.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 42:
            for x in range(5000):
                a = [210.03, 210.04, 210.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 43:
            for x in range(5000):
                a = [450.3, 450.4, 450.5]
                b = a[x%3]
                z = math.cos(b)
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b*z)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b*z)
        elif num == 44:
            for x in range(5000):
                a = [160.03, 170.04, 180.05]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
        elif num == 45:
            for x in range(5000):
                a = [560.3, 570.4, 580.5]
                b = a[x%3]
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 1000 + 1)
                ninja.forward(x)
                ninja.left(b)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 1000 + 1)
                ninja2.forward(x)
                ninja2.right(b)
            screen.update()
        elif num == 46:
            for x in range(5000):
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.right(61)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 500 + 1)
                ninja2.backward(x)
                ninja2.left(161)
            screen.update()

    @staticmethod
    def spiralSquare12():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("11 Mirror Images")
        t=Turtle()
        t.screen.bgcolor('black')
        print("You have 11 different mirror images to choose from.")
        num = random.randrange(1, 12)
        print("This is mirror image number", num)
        ninja = turtle.Turtle()
        t.hideturtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        ninja2 = turtle.Turtle()
        ninja2.speed(0)
        ninja3 = turtle.Turtle()
        ninja3.speed(0)
        ninja4 = turtle.Turtle()
        ninja4.speed(0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        colors2 = ['Forest Green', 'DeepPink']
        colors3 = ['Silver', 'medium blue']
        colors4 = ['yellow', 'DeepPink']
        colors5 = ['hot pink', 'medium blue']
        if num == 1:
            for x in range(5000):
                ninja.pencolor(colors[x % 6])
                ninja.setposition(400, 0)
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(250)
                ninja.back(x)
                ninja.right(0.05)
                ninja.forward(x)
                ninja.left(60)
                ninja.back(x)
                ninja2.pencolor(colors[x % 6])
                ninja2.setposition(-400, 0)
                ninja2.width(x / 500 + 1)
                ninja2.forward(x)
                ninja2.circle(250)
                ninja2.back(x)
                ninja2.right(0.05)
                ninja2.forward(x)
                ninja2.left(60)
                ninja2.back(x)
                ninja3.pencolor(colors3[x % 2])
                ninja3.setposition(400, 0)
                ninja3.width(x / 500 + 1)
                ninja3.forward(x)
                ninja3.circle(150)
                ninja3.back(x)
                ninja3.left(0.05)
                ninja3.forward(x)
                ninja3.right(90)
                ninja3.back(x)
                ninja4.pencolor(colors3[x % 2])
                ninja4.setposition(-400, 0)
                ninja4.width(x / 500 + 1)
                ninja4.forward(x)
                ninja4.circle(150)
                ninja4.back(x)
                ninja4.left(0.05)
                ninja4.forward(x)
                ninja4.right(90)
                ninja4.back(x)
        elif num == 2:
            for x in range(5000):
                ninja.pencolor(colors[x % 6])
                ninja.setposition(400, 0)
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(250)
                ninja.back(x)
                ninja.right(0.05)
                ninja.forward(x)
                ninja.left(60)
                ninja.back(x)
                ninja2.pencolor(colors[x % 6])
                ninja2.setposition(-400, 0)
                ninja2.width(x / 500 + 1)
                ninja2.back(x)
                ninja2.circle(250)
                ninja2.forward(x)
                ninja2.left(0.05)
                ninja2.back(x)
                ninja2.right(60)
                ninja2.forward(x)
                ninja3.pencolor(colors3[x % 2])
                ninja3.setposition(400, 0)
                ninja3.width(x / 500 + 1)
                ninja3.forward(x)
                ninja3.circle(150)
                ninja3.back(x)
                ninja3.left(0.05)
                ninja3.forward(x)
                ninja3.right(90)
                ninja3.back(x)
                ninja4.pencolor(colors3[x % 2])
                ninja4.setposition(-400, 0)
                ninja4.width(x / 500 + 1)
                ninja4.back(x)
                ninja4.circle(150)
                ninja4.forward(x)
                ninja4.right(0.05)
                ninja4.back(x)
                ninja4.left(90)
                ninja4.forward(x)
        elif num == 3:
            for x in range(5000):
                ninja.pencolor(colors[x % 6])
                ninja.setposition(400, 0)
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(250)
                ninja.back(x)
                ninja.right(0.05)
                ninja.forward(x)
                ninja.left(520)
                ninja.back(x)
                ninja2.pencolor(colors[x % 6])
                ninja2.setposition(-400, 0)
                ninja2.width(x / 500 + 1)
                ninja2.back(x)
                ninja2.circle(250)
                ninja2.forward(x)
                ninja2.left(0.05)
                ninja2.back(x)
                ninja2.right(520)
                ninja2.forward(x)
                ninja3.pencolor(colors3[x % 2])
                ninja3.setposition(400, 0)
                ninja3.width(x / 500 + 1)
                ninja3.forward(x)
                ninja3.circle(150)
                ninja3.back(x)
                ninja3.left(0.05)
                ninja3.forward(x)
                ninja3.right(290)
                ninja3.back(x)
                ninja4.pencolor(colors3[x % 2])
                ninja4.setposition(-400, 0)
                ninja4.width(x / 500 + 1)
                ninja4.back(x)
                ninja4.circle(150)
                ninja4.forward(x)
                ninja4.right(0.05)
                ninja4.back(x)
                ninja4.left(290)
                ninja4.forward(x)
        elif num == 4:
            for x in range(5000):
                ninja.pencolor(colors[x % 6])
                ninja.setposition(400, 0)
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(250)
                ninja.back(x)
                ninja.right(0.05)
                ninja.forward(x)
                ninja.left(70)
                ninja.back(x)
                ninja2.pencolor(colors[x % 6])
                ninja2.setposition(-400, 0)
                ninja2.width(x / 500 + 1)
                ninja2.back(x)
                ninja2.circle(250)
                ninja2.forward(x)
                ninja2.left(0.05)
                ninja2.back(x)
                ninja2.right(70)
                ninja2.forward(x)
                ninja3.pencolor(colors2[x % 2])
                ninja3.setposition(400, 0)
                ninja3.width(x / 500 + 1)
                ninja3.forward(x)
                ninja3.circle(150)
                ninja3.back(x)
                ninja3.left(0.05)
                ninja3.forward(x)
                ninja3.right(500)
                ninja3.back(x)
                ninja4.pencolor(colors2[x % 2])
                ninja4.setposition(-400, 0)
                ninja4.width(x / 500 + 1)
                ninja4.back(x)
                ninja4.circle(150)
                ninja4.forward(x)
                ninja4.right(0.05)
                ninja4.back(x)
                ninja4.left(500)
                ninja4.forward(x)
        elif num == 5:
            for x in range(5000):
                ninja.pencolor(colors[x % 6])
                ninja.setposition(400, 0)
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(250)
                ninja.back(x)
                ninja.right(0.05)
                ninja.forward(x)
                ninja.left(90)
                ninja.back(x)
                ninja2.pencolor(colors[x % 6])
                ninja2.setposition(-400, 0)
                ninja2.width(x / 500 + 1)
                ninja2.back(x)
                ninja2.circle(250)
                ninja2.forward(x)
                ninja2.left(0.05)
                ninja2.back(x)
                ninja2.right(90)
                ninja2.forward(x)
                ninja3.pencolor(colors2[x % 2])
                ninja3.setposition(400, 0)
                ninja3.width(x / 500 + 1)
                ninja3.forward(x)
                ninja3.circle(150)
                ninja3.back(x)
                ninja3.left(0.05)
                ninja3.forward(x)
                ninja3.right(90)
                ninja3.back(x)
                ninja4.pencolor(colors2[x % 2])
                ninja4.setposition(-400, 0)
                ninja4.width(x / 500 + 1)
                ninja4.back(x)
                ninja4.circle(150)
                ninja4.forward(x)
                ninja4.right(0.05)
                ninja4.back(x)
                ninja4.left(90)
                ninja4.forward(x)
        elif num == 6:
            for x in range(5000):
                ninja.pencolor(colors4[x % 2])
                ninja.setposition(400, 0)
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(250)
                ninja.back(x)
                ninja.right(0.05)
                ninja.forward(x)
                ninja.left(180)
                ninja.back(x)
                ninja2.pencolor(colors3[x % 2])
                ninja2.setposition(-400, 0)
                ninja2.width(x / 500 + 1)
                ninja2.back(x)
                ninja2.circle(250)
                ninja2.forward(x)
                ninja2.left(0.05)
                ninja2.back(x)
                ninja2.right(180)
                ninja2.forward(x)
                ninja3.pencolor(colors[x % 6])
                ninja3.setposition(400, 0)
                ninja3.width(x / 500 + 1)
                ninja3.forward(x)
                ninja3.circle(150)
                ninja3.back(x)
                ninja3.left(0.05)
                ninja3.forward(x)
                ninja3.right(30)
                ninja3.back(x)
                ninja4.pencolor(colors[x % 6])
                ninja4.setposition(-400, 0)
                ninja4.width(x / 500 + 1)
                ninja4.back(x)
                ninja4.circle(150)
                ninja4.forward(x)
                ninja4.right(0.05)
                ninja4.back(x)
                ninja4.left(30)
                ninja4.forward(x)
        elif num == 7:
            for x in range(5000):
                a = [30.3, 30.4, 30.5]
                b = a[x%3]
                ninja.pencolor(colors5[x % 2])
                ninja.setposition(400, 0)
                ninja.width(x / 500 + 1)
                ninja.forward(x+x)
                ninja.circle(50)
                ninja.back(x)
                ninja.right(0.05)
                ninja.forward(x)
                ninja.left(b+b)
                ninja.back(x)
                ninja2.pencolor(colors5[x % 2])
                ninja2.setposition(-400, 0)
                ninja2.width(x / 500 + 1)
                ninja2.back(x+x)
                ninja2.circle(50)
                ninja2.forward(x)
                ninja2.left(0.05)
                ninja2.back(x)
                ninja2.right(b+b)
                ninja2.forward(x)
                ninja3.pencolor(colors[x % 6])
                ninja3.setposition(400, 0)
                ninja3.width(x / 500 + 1)
                ninja3.forward(x+x)
                ninja3.circle(25)
                ninja3.back(x)
                ninja3.left(0.05)
                ninja3.forward(x)
                ninja3.right(b+b)
                ninja3.back(x)
                ninja4.pencolor(colors[x % 6])
                ninja4.setposition(-400, 0)
                ninja4.width(x / 500 + 1)
                ninja4.back(x+x)
                ninja4.circle(25)
                ninja4.forward(x)
                ninja4.right(0.05)
                ninja4.back(x)
                ninja4.left(b+b)
                ninja4.forward(x)
        elif num == 8:
            for x in range(5000):
                a = [60.3, 60.4, 60.5]
                b = a[x%3]
                ninja.pencolor(colors3[x % 2])
                ninja.setposition(400, 0)
                ninja.width(x / 500 + 1)
                ninja.forward(x+x)
                ninja.dot(15)
                ninja.back(x)
                ninja.right(0.05)
                ninja.forward(x)
                ninja.left(b+b+b)
                ninja.back(x)
                ninja2.pencolor(colors3[x % 2])
                ninja2.setposition(-400, 0)
                ninja2.width(x / 500 + 1)
                ninja2.back(x+x)
                ninja2.dot(15)
                ninja2.forward(x)
                ninja2.left(0.05)
                ninja2.back(x)
                ninja2.right(b+b+b)
                ninja2.forward(x)
                ninja3.pencolor(colors[x % 6])
                ninja3.setposition(400, 0)
                ninja3.width(x / 500 + 1)
                ninja3.forward(x+x)
                ninja3.dot(10)
                ninja3.back(x)
                ninja3.left(0.05)
                ninja3.forward(x)
                ninja3.right(b+b+b)
                ninja3.back(x)
                ninja4.pencolor(colors[x % 6])
                ninja4.setposition(-400, 0)
                ninja4.width(x / 500 + 1)
                ninja4.back(x+x)
                ninja4.dot(10)
                ninja4.forward(x)
                ninja4.right(0.05)
                ninja4.back(x)
                ninja4.left(b+b+b)
                ninja4.forward(x)
            screen.update()
        elif num == 9:
            for x in range(5000):
                ninja.pencolor(colors[x % 6])
                ninja.setposition(600, 0)
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(1000)
                ninja.back(x)
                ninja.right(30)
                ninja.forward(x)
                ninja.left(15)
                ninja.back(x)
                ninja2.pencolor(colors[x % 6])
                ninja2.setposition(-600, 0)
                ninja2.width(x / 500 + 1)
                ninja2.back(x)
                ninja2.circle(1000)
                ninja2.forward(x)
                ninja2.left(30)
                ninja2.back(x)
                ninja2.right(15)
                ninja2.forward(x)
            screen.update()
        elif num == 10:
            for x in range(5000):
                a = 120
                b = 15
                ninja.pencolor(colors[x % 6])
                ninja.setposition(600, 0)
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(10000)
                ninja.back(x)
                ninja.right(a)
                ninja.forward(x)
                ninja.left(b)
                ninja.back(x)
                ninja2.pencolor(colors[x % 6])
                ninja2.setposition(-600, 0)
                ninja2.width(x / 500 + 1)
                ninja2.back(x)
                ninja2.circle(10000)
                ninja2.forward(x)
                ninja2.left(a)
                ninja2.back(x)
                ninja2.right(b)
                ninja2.forward(x)
                ninja3.pencolor(colors[x % 6])
                ninja3.setposition(0, 0)
                ninja3.width(x / 500 + 1)
                ninja3.back(x)
                ninja3.circle(10000)
                ninja3.forward(x)
                ninja3.left(a)
                ninja3.back(x)
                ninja3.right(b)
                ninja3.forward(x)
                ninja4.pencolor(colors[x % 6])
                ninja4.setposition(0, 0)
                ninja4.width(x / 500 + 1)
                ninja4.forward(x)
                ninja4.circle(10000)
                ninja4.back(x)
                ninja4.right(a)
                ninja4.forward(x)
                ninja4.left(b)
                ninja4.back(x)
            screen.update()
        elif num == 11:
            for x in range(5000):
                a = 120
                b = 15
                ninja.pencolor(colors[x % 6])
                ninja.setposition(600, 0)
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(100)
                ninja.back(x)
                ninja.right(a)
                ninja.forward(x)
                ninja.left(b)
                ninja.back(x)
                ninja2.pencolor(colors[x % 6])
                ninja2.setposition(-600, 0)
                ninja2.width(x / 500 + 1)
                ninja2.back(x)
                ninja2.circle(100)
                ninja2.forward(x)
                ninja2.left(a)
                ninja2.back(x)
                ninja2.right(b)
                ninja2.forward(x)
                ninja3.pencolor(colors[x % 6])
                ninja3.setposition(0, 0)
                ninja3.width(x / 500 + 1)
                ninja3.back(x)
                ninja3.circle(100)
                ninja3.forward(x)
                ninja3.left(a)
                ninja3.back(x)
                ninja3.right(b)
                ninja3.forward(x)
                ninja4.pencolor(colors[x % 6])
                ninja4.setposition(0, 0)
                ninja4.width(x / 500 + 1)
                ninja4.forward(x)
                ninja4.circle(100)
                ninja4.back(x)
                ninja4.right(a)
                ninja4.forward(x)
                ninja4.left(b)
                ninja4.back(x)
            screen.update()

    @staticmethod
    def spiralSquare13():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("Three 1970's Disco Designs")
        t=Turtle()
        t.screen.bgcolor('black')
        num = random.randrange(1, 4)
        print("This is disco design number", num)
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        t.hideturtle()
        ninja.speed(0)
        ninja.setposition(600, 0)
        ninja2 = turtle.Turtle()
        ninja2.speed(0)
        ninja2.setposition(-600, 0)
        ninja3 = turtle.Turtle()
        ninja3.speed(0)
        ninja3.setposition(0, 0)
        ninja4 = turtle.Turtle()
        ninja4.speed(0)
        ninja4.setposition(0, 0)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        if num == 1:
            for x in range(5000):
                a = 120
                b = 30
                c = 60
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(100)
                ninja.back(x)
                ninja.right(a)
                ninja.forward(x)
                ninja.left(c)
                ninja.back(x)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 500 + 1)
                ninja2.back(x)
                ninja2.circle(100)
                ninja2.forward(x)
                ninja2.left(a)
                ninja2.back(x)
                ninja2.right(c)
                ninja2.forward(x)
                ninja3.pencolor(colors[x % 6])
                ninja3.width(x / 500 + 1)
                ninja3.back(x)
                ninja3.circle(100)
                ninja3.forward(x)
                ninja3.left(a)
                ninja3.back(x)
                ninja3.right(b)
                ninja3.forward(x)
                ninja4.pencolor(colors[x % 6])
                ninja4.width(x / 500 + 1)
                ninja4.forward(x)
                ninja4.circle(100)
                ninja4.back(x)
                ninja4.right(a)
                ninja4.forward(x)
                ninja4.left(b)
                ninja4.back(x)
            screen.update()
        elif num == 2:
            for x in range(5000):
                a = 120
                b = 60
                c = 330
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(random.randrange(50))
                ninja.back(x)
                ninja.right(a)
                ninja.forward(x)
                ninja.left(c)
                ninja.back(x)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 500 + 1)
                ninja2.back(x)
                ninja2.circle(random.randrange(50))
                ninja2.forward(x)
                ninja2.left(a)
                ninja2.back(x)
                ninja2.right(c)
                ninja2.forward(x)
                ninja3.pencolor(colors[x % 6])
                ninja3.width(x / 500 + 1)
                ninja3.back(x)
                ninja3.circle(100)
                ninja3.forward(x)
                ninja3.left(a)
                ninja3.back(x)
                ninja3.right(b)
                ninja3.forward(x)
                ninja4.pencolor(colors[x % 6])
                ninja4.width(x / 500 + 1)
                ninja4.forward(x)
                ninja4.circle(100)
                ninja4.back(x)
                ninja4.right(a)
                ninja4.forward(x)
                ninja4.left(b)
                ninja4.back(x)
            screen.update()
        elif num == 3:
            for x in range(5000):
                a = 90
                b = 60
                c = 30
                ninja.pencolor(colors[x % 6])
                ninja.width(x / 500 + 1)
                ninja.forward(x)
                ninja.circle(random.randrange(50))
                ninja.back(x)
                ninja.right(a)
                ninja.forward(x)
                ninja.left(c)
                ninja.back(x)
                ninja2.pencolor(colors[x % 6])
                ninja2.width(x / 500 + 1)
                ninja2.back(x)
                ninja2.circle(random.randrange(50))
                ninja2.forward(x)
                ninja2.left(a)
                ninja2.back(x)
                ninja2.right(c)
                ninja2.forward(x)
                ninja3.pencolor(colors[x % 6])
                ninja3.width(x / 500 + 1)
                ninja3.back(x)
                ninja3.circle(50)
                ninja3.forward(x)
                ninja3.left(a)
                ninja3.back(x)
                ninja3.right(b)
                ninja3.forward(x)
                ninja4.pencolor(colors[x % 6])
                ninja4.width(x / 500 + 1)
                ninja4.forward(x)
                ninja4.circle(50)
                ninja4.back(x)
                ninja4.right(a)
                ninja4.forward(x)
                ninja4.left(b)
                ninja4.back(x)
            screen.update()

    @staticmethod
    def spiralSquare14():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("32 Convergences")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('gray')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        ninja.setposition(0, 0)
        ninja2 = turtle.Turtle()
        ninja2.speed(0)
        ninja2.setposition(-0, 0)
        colors = ['red', 'green', 'yellow', 'purple', 'orange', 'blue']
        colors3 = ['green', 'yellow', 'red', 'purple', 'black', 'white']
        colors4 = ['deep pink', 'DarkViolet', 'DarkGreen', 'SaddleBrown', 'deep sky blue', 'OrangeRed']
        a1 = [151, 251, 951]
        a2 = [50, 90, 120]
        a3 = [90, 100.1, 110.2]
        a4 = [80, 90.1, 100.2]
        a5 = [81, 91.1, 101.2]
        a6 = [79, 89.1, 99.2]
        a7 = [75, 85.1, 95.2]
        a8 = [70, 80.1, 90.2]
        a9 = [65, 80.1, 90.2]
        a10 = [65, 70.1, 90.2]
        a11 = [55, 60.1, 90.2]
        a12 = [65, 80.1, 80.2]
        a13 = [70, 80.1, 80.2]
        a14 = [71, 80.1, 80.2]
        a15 = [74, 80.1, 80.2]
        a16 = [80, 80.1, 80.2]
        a17 = [81, 80.1, 80.2]
        a18 = [85, 80.1, 80.2]
        a19 = [90, 80.1, 80.2]
        a20 = [91, 80.1, 80.2]
        a21 = [95, 80.1, 80.2]
        a22 = [100, 80.1, 80.2]
        a23 = [60, 15.1, 15.2]
        a24 = [75, 15.1, 15.2]
        a25 = [240, 15.1, 15.2]
        a26 = [61, 60.1, 60.2]
        a27 = [120, 60.1, 60.2]
        a28 = [180, 60.1, 60.2]
        a29 = [105, 85.1, 95.2]
        a30 = [135, 85.1, 95.2]
        a31 = [225, 117.1, 93.2]
        a32 = [51, 91, 121]
        list = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32]
        random_num = random.choice(list)
        print("\n32 different convergence designs to choose from.")
        print("\nThis is convergence design: ", random_num)
        for x in range(5000):
            a = random_num
            b = a[x%3]
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x)
            ninja.right(b)
            ninja.right(b)
            ninja.forward(x)
            ninja.pencolor(colors3[x % 6])
            ninja.dot(10)
            ninja.pencolor(colors4[x % 6])
            ninja.circle(10)
            ninja2.pencolor(colors[x % 6])
            ninja2.width(x / 500 + 1)
            ninja2.backward(x)
            ninja2.left(b)
            ninja2.left(b)
            ninja2.backward(x)
            ninja2.pencolor(colors3[x % 6])
            ninja2.dot(10)
            ninja2.pencolor(colors4[x % 6])
            ninja2.circle(10)
        screen.update()

    @staticmethod
    def spiralSquare15():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("32 Convergences Permutated")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('gray')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        ninja.setposition(0, 0)
        ninja2 = turtle.Turtle()
        ninja2.speed(0)
        ninja2.setposition(-0, 0)
        colors4 = ['red', 'green', 'yellow', 'purple', 'orange', 'blue']
        colors3 = ['green', 'yellow', 'red', 'purple', 'black', 'white']
        colors = ['deep pink', 'DarkViolet', 'DarkGreen', 'SaddleBrown', 'deep sky blue', 'OrangeRed']
        a1 = [151, 251, 951]
        a2 = [50, 90, 120]
        a3 = [90, 100.1, 110.2]
        a4 = [80, 90.1, 100.2]
        a5 = [81, 91.1, 101.2]
        a6 = [79, 89.1, 99.2]
        a7 = [75, 85.1, 95.2]
        a8 = [70, 80.1, 90.2]
        a9 = [65, 80.1, 90.2]
        a10 = [65, 70.1, 90.2]
        a11 = [55, 60.1, 90.2]
        a12 = [65, 80.1, 80.2]
        a13 = [70, 80.1, 80.2]
        a14 = [71, 80.1, 80.2]
        a15 = [74, 80.1, 80.2]
        a16 = [80, 80.1, 80.2]
        a17 = [81, 80.1, 80.2]
        a18 = [85, 80.1, 80.2]
        a19 = [90, 80.1, 80.2]
        a20 = [91, 80.1, 80.2]
        a21 = [95, 80.1, 80.2]
        a22 = [100, 80.1, 80.2]
        a23 = [60, 15.1, 15.2]
        a24 = [75, 15.1, 15.2]
        a25 = [240, 15.1, 15.2]
        a26 = [61, 60.1, 60.2]
        a27 = [120, 60.1, 60.2]
        a28 = [180, 60.1, 60.2]
        a29 = [105, 85.1, 95.2]
        a30 = [135, 85.1, 95.2]
        a31 = [225, 117.1, 93.2]
        a32 = [51, 91, 121]
        list1 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32]
        random_num = random.choice(list1)
        list2 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32]
        random_num2 = random.choice(list2)
        print("\nPermutations on the 32 Convergence designs by adding them together.")
        print("\nThis is convergence design", random_num, "and convergence design", random_num2)
        for x in range(5000):
            a = random_num
            b = a[x%3]
            c = random_num2
            d = c[x%3]
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x+d)
            ninja.right(b)
            ninja.right(b)
            ninja.forward(x+d)
            ninja.pencolor(colors3[x % 6])
            ninja.dot(10)
            ninja.pencolor(colors4[x % 6])
            ninja.circle(10)
            ninja2.pencolor(colors[x % 6])
            ninja2.width(x / 500 + 1)
            ninja2.backward(x+d)
            ninja2.left(b)
            ninja2.left(b)
            ninja2.backward(x+d)
            ninja2.pencolor(colors3[x % 6])
            ninja2.dot(10)
            ninja2.pencolor(colors4[x % 6])
            ninja2.circle(10)
        screen.update()

    @staticmethod
    def spiralSquare16():
        screen = turtle.Screen()
        wn = turtle.Screen()
        wn.title("32 Convergences Permutated Variations")
        t=Turtle()
        t.hideturtle()
        t.screen.bgcolor('black')
        ninja = turtle.Turtle()
        screen.tracer(18, 2)
        ninja.speed(0)
        ninja.setposition(0, 0)
        ninja2 = turtle.Turtle()
        ninja2.speed(0)
        ninja2.setposition(-0, 0)
        colors4 = ['red', 'green', 'yellow', 'purple', 'orange', 'blue']
        colors3 = ['green', 'yellow', 'red', 'purple', 'gray', 'white']
        colors = ['deep pink', 'DarkViolet', 'DarkGreen', 'SaddleBrown', 'deep sky blue', 'OrangeRed']
        a1 = [151, 251, 951]
        a2 = [50, 90, 120]
        a3 = [90, 100.1, 110.2]
        a4 = [80, 90.1, 100.2]
        a5 = [81, 91.1, 101.2]
        a6 = [79, 89.1, 99.2]
        a7 = [75, 85.1, 95.2]
        a8 = [70, 80.1, 90.2]
        a9 = [65, 80.1, 90.2]
        a10 = [65, 70.1, 90.2]
        a11 = [55, 60.1, 90.2]
        a12 = [65, 80.1, 80.2]
        a13 = [70, 80.1, 80.2]
        a14 = [71, 80.1, 80.2]
        a15 = [74, 80.1, 80.2]
        a16 = [80, 80.1, 80.2]
        a17 = [81, 80.1, 80.2]
        a18 = [85, 80.1, 80.2]
        a19 = [90, 80.1, 80.2]
        a20 = [91, 80.1, 80.2]
        a21 = [95, 80.1, 80.2]
        a22 = [100, 80.1, 80.2]
        a23 = [60, 15.1, 15.2]
        a24 = [75, 15.1, 15.2]
        a25 = [240, 15.1, 15.2]
        a26 = [61, 60.1, 60.2]
        a27 = [120, 60.1, 60.2]
        a28 = [180, 60.1, 60.2]
        a29 = [105, 85.1, 95.2]
        a30 = [135, 85.1, 95.2]
        a31 = [225, 117.1, 93.2]
        a32 = [51, 91, 121]
        list1 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32]
        random_num = random.choice(list1)
        list2 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32]
        random_num2 = random.choice(list2)
        print("\nPermutations on the 32 Convergence designs by adding them together.")
        print("\nThis is convergence design", random_num, "and convergence design", random_num2)
        random_num3 = random.randrange(1, 4)
        for x in range(5000):
            a = random_num
            b = a[x%3]
            c = random_num2
            d = c[x%3]
            e = random_num3
            ninja.pencolor(colors[x % 6])
            ninja.width(x / 500 + 1)
            ninja.forward(x+d/e)
            ninja.right(b)
            ninja.right(b)
            ninja.forward(x+d*e)
            ninja.pencolor(colors3[x % 6])
            ninja.dot(10)
            ninja.pencolor(colors4[x % 6])
            ninja.circle(10)
            ninja2.pencolor(colors[x % 6])
            ninja2.width(x / 500 + 1)
            ninja2.backward(x+d/e)
            ninja2.left(b)
            ninja2.left(b)
            ninja2.backward(x+d*e)
            ninja2.pencolor(colors3[x % 6])
            ninja2.dot(10)
            ninja2.pencolor(colors4[x % 6])
            ninja2.circle(10)
        screen.update()
              
# ==============================================================================================================================
# Spiral Square functions

def spiral_square():
    print("\nSPIRAL DESIGNS")
    print("\nA collection of 31 algorithms that produce different spiral designs")
    print("\nSelect a design.")
    print("\n1. Triangle Attack")
    print("2. Space Flower")
    print("3. Dimensions of Lines")
    print("4. The Brilliance from Within")
    print("5. Trump Death Spirals")
    print("6. Higgs Boson")
    print("7. Riding the wave of the Explosion")
    print("8. The Emergent Phenomena")
    print("9. Tropical Christmas")
    print("10. The Eye of Chaos")
    print("11. 46 in One")
    print("12. 11 Mirror Images")
    print("13. Three 1970's Disco Designs")
    print("14. 32 Convergences")
    print("15. 32 Convergences Permutated")
    print("16. 32 Convergences Permutated Variations")
    
    choice = input("\nEnter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16): ")

    if choice == '1':
        Spiral_Square.spiralSquare1()

    elif choice == '2':
        Spiral_Square.spiralSquare2()

    elif choice == '3':
        Spiral_Square.spiralSquare3()

    elif choice == '4':
        Spiral_Square.spiralSquare4()

    elif choice == '5':
        Spiral_Square.spiralSquare5()

    elif choice == '6':
        Spiral_Square.spiralSquare6()

    elif choice == '7':
        Spiral_Square.spiralSquare7()

    elif choice == '8':
        Spiral_Square.spiralSquare8()

    elif choice == '9':
        Spiral_Square.spiralSquare9()

    elif choice == '10':
        Spiral_Square.spiralSquare10()

    elif choice == '11':
        Spiral_Square.spiralSquare11()

    elif choice == '12':
        Spiral_Square.spiralSquare12()

    elif choice == '13':
        Spiral_Square.spiralSquare13()

    elif choice == '14':
        Spiral_Square.spiralSquare14()

    elif choice == '15':
        Spiral_Square.spiralSquare15()

    elif choice == '16':
        Spiral_Square.spiralSquare16()

# ==============================================================================================================================
# Main Global Menu

while True:
    print("\nWelcome to Bruce's Turtle Graphics Design Program 1.0")
    print("\n1. Spiral Designs")
    print("\n2. About this program")

    choice = input("\nEnter choice(1/2): ")

    if choice == '1':
        spiral_square()

    elif choice == '2':
        a = """\nVersion 2.0 of my Python Design Program 1.0"""
        print(a)

    while True:
        answer = input('\nRun Turtle Graphics Design Program again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break





