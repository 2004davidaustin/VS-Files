import random


kidsmeal = float(input("\n\n" + "How much is the kids meal? $"))
adultmeal = float(input("How much is the adult meal? $"))
children = int(input("How many children want to order? "))
adults = int(input("How many adults want to order? "))

randkids = random.randrange(1, children)
print(f"It looks like {randkids} of the kids want cookies")
cookie = float(input("How much does the cookie cost? "))

tax = float(input("What is the tax rate? "))



subtotal = (kidsmeal * children) + (adultmeal * adults) + (randkids * cookie)
salestax = (subtotal * tax) / 100
total = subtotal + salestax



print("\n=================")
print(f"Subtotal: ${subtotal}")
print(f"Sales Tax: ${salestax}")
print(f"Total: ${total}\n")
payment = float(input("What is your payment amount? $"))
print("=================\n")



while payment < total:
    print(f"You need to pay more than that. Your remaning balance is ${total - payment}")
    payment2 = float(input("$ "))
    payment += payment2

if payment == total:
    print("Thank you! Enjoy your food." + "\n\n")

if payment > total:
    print(f"Your change is: ${payment - total}" + "\n\n")


