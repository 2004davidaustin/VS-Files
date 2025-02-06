import math

print("\n" + "====VELOCITY CALCULATOR====")
m = float(input("Mass? (in kg): "))
g = float(input("Gravity? (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time? (in seconds): "))
p = float(input("Fluid Density? (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross Sectional Area? (in m^2): "))
C = float(input("Drag Constant? (0.5 for sphere, 1.1 for cylinder): "))
print()

c = (1 / 2) * p * A * C

#v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))

v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

print(f"The inner value of c is: {c:.3f}")
print(f"The speed after {t} seconds was {v:.3f} m/s")
print("\n")