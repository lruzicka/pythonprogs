#!/usr/bin/python3

import turtle
okno = turtle.Screen()
okno.title("Turtle Keys")

zelva = turtle.Turtle()
zelva.speed(0)

krok = 2

zelva.left(90)

def vpred():
    zelva.forward(krok)

def vzad():
    zelva.backward(krok)
    
def levo():
    zelva.left(90)

def pravo():
    zelva.right(90)
    
def sbohem():
    turtle.bye()

okno.onkey(vpred, "Up")
okno.onkey(levo, "Left")
okno.onkey(pravo, "Right")
okno.onkey(vzad, "Down")
okno.onkey(sbohem, "q")

okno.listen()
