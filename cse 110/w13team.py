import math

def square(side) : return side**2
def rect(side1, side2) : return side1 * side2
def circle(diameter) : return math.pi*(diameter/2)**2

answer = ""
math_answer = ""

while answer != "quit" : 

    answer = input("What chu want bro ")

    if answer == "square" : math_answer = square(int(input("how long that boy ")))
    if answer == "rectangle" : math_answer = rect(int(input("how wide that boy ")), int(input("how tall that boy ")))
    if answer == "circle" : math_answer = circle(int(input("how wide that boy ")))

    print(f"THE AREA IS {math_answer}")
    
    