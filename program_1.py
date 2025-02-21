#Timothy Foster, 2/20/25, Kilometer Conversion Program

#Define the function.
def kilometer_conversion():

    #Define the variables.
    miles = 0.0
    kilometers = 0.0

    #Get user input.
    kilometers = int(input("Enter the number of kilometers you would like to convert."))

    #Do the conversion using the formula.
    miles = kilometers * 0.6214

    #Print the results and prevent it from being too lengthy.
    print(f"{kilometers} kilometers is equal to{miles: .3f} miles")

kilometer_conversion()
