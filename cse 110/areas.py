import math

sidesquare = float(input("\n\nWhat's the length of the square in cm? "))
print(f"The area of the square is {sidesquare**2}cm^2 or {(sidesquare**2)/10000}m^2\n")

rectwidth = float(input("What's the width of the rectangle in cm? "))
rectlength = float(input("What's the length of the rectangle in cm? "))
print(f"The area of the rectangle is {rectwidth*rectlength}cm^2 or {(rectwidth*rectlength)/10000}m^2\n")

circleradius = float(input("What's the radius of the circle in cm? "))
print(f"The area of the circle is {math.pi*circleradius**2}cm^2 or {(math.pi*circleradius**2)/10000}m^2\n")

randlength = float(input("What's a cool length in feet? "))
print(f"The area of a square would be {randlength**2}ft^2")
print(f"The area of a circle would be {math.pi*randlength**2}ft^2")
print(f"The volume of a cube would be {randlength**3}ft^2")
print(f"The volume of a sphere would be {(4/3)*math.pi*randlength**3}ft^2\n\n")