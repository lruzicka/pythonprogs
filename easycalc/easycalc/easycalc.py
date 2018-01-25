#!/usr/bin/env python3

import sys

def calc(expression):
    return(eval(expression))

def out(text):
    for line in text:
        print(line)

welcome = ["A very simple calculator",
           "----------------------------------"]
middle = ["-----------------------------------"]
bye = ["-----------------------------------", 
       "Good bye!"]

if len(sys.argv) > 1:
    print(eval(sys.argv[1]))
else:
    loop = 'y'
    out(welcome)
    while loop == 'y':
        result = eval(input("Write you expression: "))
        print("Result: ",result)
        out(middle)
        loop = input("New expression? (y/n): ")
        loop = loop.lower()
        out(bye)