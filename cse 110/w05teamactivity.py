score = float(input("What's your grade percentage? "))

if score >= 90 : grade = "n A"
elif score >= 80 : grade = " B"
elif score >= 70 : grade = " C"
elif score >= 60 : grade = " D"
elif score < 60 : grade = "n F"

print(f"\nYou got a{grade}!")

if score >= 70 : print("You passed! Congratulations!!")
elif score < 70 : print("You haven't passed yet.")