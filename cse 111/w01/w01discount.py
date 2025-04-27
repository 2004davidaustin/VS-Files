from datetime import datetime
day = datetime.now().weekday()

cost = float(input("what the cost of what chu buyin? "))

print(day)

if cost >= 50 and (day == 1 or day == 2) : 
    cost *= 0.9
    print("Today is cool day, you get 10% offhahaha")

cost *= 1.06

print(f"Heres your new cost buddy: {cost:0.2f}")