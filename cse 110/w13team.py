'''

import math

def square(side) : return side**2
def rect(side1, side2) : return side1 * side2
def circle(diameter) : return math.pi*(diameter/2)**2

answer = ""

while answer != "quit" : 

    answer = input("What do you want ")

    if answer == "square" : math_answer = square(int(input("how long is it ")))
    if answer == "rectangle" : math_answer = rect(int(input("how wide is it ")), int(input("how tall is it ")))
    if answer == "circle" : math_answer = circle(int(input("how wide is it ")))

    print(f"THE AREA IS {math_answer}")


'''
    
import math

def square(side) : return side**2
def rect(side1, side2) : return side1 * side2
def circle(diameter) : return math.pi*(diameter/2)**2

answer = ""
math_answer = 0.0

while answer != "quit" : 

    answer = input("What shape do you want to to do ").lower()

    if answer == "square" : math_answer = square(int(input("How long is it? ")))
    if answer == "rectangle" : math_answer = rect(int(input("How tall is it? ")), int(input("How wide is it? ")))
    if answer == "circle" : math_answer = circle(float(input("How big is your circle???? ")))

    print(math_answer)