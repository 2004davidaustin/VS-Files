import math

items = int(input("Number of items: "))
items_per_box = int(input("Number of items per box: "))

boxes = math.ceil(items / items_per_box)

print(f"You'll need {boxes} boxes to put {items} items in boxes that hold {items_per_box} itmes per box")