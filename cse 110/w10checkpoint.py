print("ok list bro gimme")
itemz = []
item = ""

while item != "quit" :
    item = input("gimme: ")
    itemz.append(item)
itemz.pop()

print("\nhere yo items")
for item in itemz :
    print(item)

print("\nhere yo items IN A LIST")
for i, item in enumerate(itemz) :
    print(i, item)

change_num = int(input("\nwhich yall wanna change? "))
change_name = input("whatcha wanna change it to? ")

itemz[change_num] = change_name

print("\nokis here yo items again")
for item in itemz :
    print(item)