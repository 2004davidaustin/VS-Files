#Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)

#calculators
def fahrenheit(input) : return (input * 9/5) + 32
def celsius(input) : return (input - 32) * 5/9
def miles(input) : return input * 0.62137
def windchillcalc(temp, speed) : return 35.74 + (0.6215 * temp) - 35.75 * (speed ** 0.16) + (0.4275 * temp) * (speed ** 0.16)



#inquiry
print()
temp = float(input("What's the temperature? "))
temp_type = input("Fahrenheit or celsius? (F/C) ").lower()
speed_type = input("Miles per hour or kilometers per hour? (M/K) ").lower()
print()



#one time changes depending on input
if temp_type == "f" :
    x = temp
    temp_word = "F"
elif temp_type == "c" :
    x = fahrenheit(temp)
    temp_word = "C"

if speed_type == "m" : speed_word = "mph"
elif speed_type == "k" : speed_word = "kmh"



#for loop
for speed in range(5, 65, 5) : 
    
    
    #changes that need to be repeated depending on input
    if speed_type == "k" : y = miles(speed)
    else : y = speed

    if temp_type == "f" : windchill = windchillcalc(x, y)
    elif temp_type == "c" : windchill = celsius(windchillcalc(x, y))
    

    #print it all
    print(f"At {temp}{temp_word} and {speed}{speed_word}, the windchill is {windchill:.2f}{temp_word}")
    
print()