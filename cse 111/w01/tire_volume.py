from datetime import datetime
import math



#assignment

date = datetime.now(tz=None).strftime('%Y-%m-%d')
w = float(input("Width of the tire? (mm) "))
a = float(input("Aspect ratio of the tire? "))
d = float(input("Diameter of the tire? (inches) "))

v = round((math.pi * w**2 * a * (w * a + 2540 * d)) / (10000000000), 2)
print(f"The volume is about {v} liters")

price = float(input("Price of the tire? "))

with open("volumes.txt", "at") as dataset :
    print(date, w, a, d, v, price, sep=", ", end="\n", file=dataset, flush=False)
    print(f"Printed, {date}")




#find price of a tire liter

volumes = 0
prices = 0

with open("volumes.txt") as dataset : 
    for line in dataset :
        line = line.strip()
        line = line.split(",")

        volumes += float(line[4]) 
        prices += float(line[5])

        ratio = prices / volumes
    print(f"From the list, the average price of a liter of volume in a tire is {ratio:0.2} dollars")