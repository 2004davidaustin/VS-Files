number = 1
print("yoooo welcome")
best_list = []

while number != 0 :
    number = float(input("What you number"))
    if number != 0 : best_list.append(number)

print()
print(f"Your sum is: {sum(best_list)}")
print(f"Yous average is: {sum(best_list)/len(best_list)}")
print(f"The largest number is: {max(best_list)}")
print(f"The smolest number is: {min(best_list)}")
print(f"The list sorted would be: {sorted(best_list)}")

guessnum = best_list[0]
for num in best_list :
    if num > 0 and guessnum > num : guessnum = num
print(f"THE SMALLEST POSTIVE NUMBER: {guessnum}")
