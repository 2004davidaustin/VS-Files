height = int(input("How tall are you? (In inches): "))
age = int(input("How old are you? "))

if input("Is there another person with you? (Yes or No): ").lower() == "yes" : another_person = True
else : another_person = False

if another_person :
    height2 = int(input("How tall are they? (In inches): "))
    age2 = int(input("How old are they? "))



if height < 36: they_can_ride = False

if not another_person : 
    if height >= 62 and age >= 18 : they_can_ride = True

if another_person :
    if age >= 18 or age2 >= 18 : they_can_ride = True
    if height2 < 36: they_can_ride = False



if they_can_ride : print("They can ride")
else : print("They cannot ride")