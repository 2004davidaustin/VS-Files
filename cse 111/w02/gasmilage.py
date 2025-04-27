def main() :
    odm_start = float(input("A starting odometer value in miles: "))
    odm_end = float(input("An ending odometer value in miles: "))
    gallons = float(input("An amount of fuel in gallons: "))
    mpg = miles_per_gallon(odm_start, odm_end, gallons)
    lp100k = lp100k_from_mpg(mpg)
    print(f"{mpg:0.2f} miles per gallon")
    print(f"{lp100k:0.2f} liters per 100 kilometers")
    return

def miles_per_gallon(start, end, gallons) : 
    return (end-start)/gallons

def lp100k_from_mpg(mpg) :
    return 235.215 / mpg

main()