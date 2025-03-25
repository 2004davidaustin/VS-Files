# NAME ABREVIATION YEAR LIFE-EXPECTANCY

#'''


with open("life-expectancy.csv") as dataset :

    year_chosen = input("\nEnter your year of interest: ")


    #declare them variable goons because why not
    highest_chosen = ["", "", "", "0"]
    lowest_chosen = ["", "", "", "999"] #this could be better
    average_chosen = 0
    average_counter = 0

    highest_overall = ["", "", "", "0"]
    lowest_overall = ["", "", "", "999"] #this could be better


    #for loop and clean data
    for line in dataset :
        line = line.strip()
        line = line.split(",")

        #chosen figure outers
        if year_chosen == line[2] and float(line[3]) > float(highest_chosen[3]) : highest_chosen = line
        if year_chosen == line[2] and float(line[3]) < float(lowest_chosen[3]) : lowest_chosen = line
        if year_chosen == line[2] :
            average_chosen += float(line[3])
            average_counter += 1

        #whole database figure outers
        if float(line[3]) > float(highest_overall[3]) : highest_overall = line
        if float(line[3]) < float(lowest_overall[3]) : lowest_overall = line

    #calculate average real quick
    average_chosen = average_chosen / average_counter


    print()
    print(f"{highest_chosen[0]} was the country with the highest life expectancy of {highest_chosen[3]} years in {year_chosen},")
    print(f"{lowest_chosen[0]} was the country with the lowest life expectancy of {lowest_chosen[3]} years in {year_chosen},")
    print(f"And in the year {year_chosen}, the average life expectancy across all countries was {average_chosen}.")
    print()
    print(f"In the dataset, the highest life expectancy was {highest_overall[3]} from {highest_overall[0]} in {highest_overall[2]}")
    print(f"And the lowest life expectancy was {lowest_overall[3]} years from {lowest_overall[0]} in {lowest_overall[2]}")
    print()


#'''