# NAME ABREVIATION YEAR LIFE-EXPECTANCY

#'''


with open("life-expectancy.csv") as dataset :

    year_chosen = int(input("\nEnter your year of interest: "))
    country_chosen = input("Enter your country of interest: ")

    #declare them variable goons because why not
    highest_chosen = ["", "", 0, 0]
    lowest_chosen = ["", "", 0, 999] #this could be better
    average_chosen = 0
    average_counter = 0

    highest_overall = ["", "", 0, 0]
    lowest_overall = ["", "", 0, 999] #this could be better

    highest_country = ["", "", 0, 0]
    lowest_country = ["", "", 0, 999] #this could be better

    country_found = ["", "", 0, 0]

    change = ""


    #for loop and clean data
    for line in dataset :
        line = line.strip()
        line = line.split(",")
        line[2] = int(line[2])
        line[3] = float(line[3])

        #chosen country figure outers
        if country_chosen.lower() == line[0].lower() : 
            if year_chosen == line[2] : country_found = line
            if (year_chosen + 1) == line[2] : country_next = line
            if line[3] > highest_country[3] : highest_country = line
            if line[3] < lowest_country[3] : lowest_country = line

        #chosen year figure outers
        if year_chosen == line[2] :
            if line[3] > highest_chosen[3] : highest_chosen = line
            if line[3] < lowest_chosen[3] : lowest_chosen = line
            average_chosen += line[3]
            average_counter += 1

        #whole database figure outers
        if line[3] > highest_overall[3] : highest_overall = line
        if line[3] < lowest_overall[3] : lowest_overall = line

    #calculate john real quick
    if country_found[3] < country_next[3] : change = "increased"
    else : change = "decreased"

    average_chosen = average_chosen / average_counter

    

    print()
    print(f"In {year_chosen}, {country_found[0]} had a life expectancy of {country_found[3]:.2f} and {change} the following year.")
    print(f"In {country_found[0]}, the highest life expectancy was {highest_country[3]:.2f} in the year {highest_country[2]},")
    print(f"And the lowest life expectancy was {lowest_country[3]:.2f} in the year {lowest_country[2]}.")
    print()
    print(f"{highest_chosen[0]} was the country with the highest life expectancy of {highest_chosen[3]:.2f} years in {year_chosen},")
    print(f"{lowest_chosen[0]} was the country with the lowest life expectancy of {lowest_chosen[3]:.2f} years in {year_chosen},")
    print(f"And in the year {year_chosen}, the average life expectancy across all countries was {average_chosen:.2f}.")
    print()
    print(f"In the dataset, the highest life expectancy was {highest_overall[3]:.2f} from {highest_overall[0]} in {highest_overall[2]}")
    print(f"And the lowest life expectancy was {lowest_overall[3]:.2f} years from {lowest_overall[0]} in {lowest_overall[2]}")
    print()


#'''