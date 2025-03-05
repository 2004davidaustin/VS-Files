name = ""
namelist = []
while name != "end" :
    name = input("Namebro gimmie: ")
    if name != "end" : namelist.append(name)

print("your frineds are:::: ")
for s in namelist : 
    print(s)