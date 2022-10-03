class Functions():

    def Temperature():
        
        temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C) : ")
        
        degree = int(temp[:-1])
        
        i_convention = temp[-1]

        if i_convention.upper() == "C":
            result = int(round((9 * degree) / 5 + 32))
            o_convention = "Fahrenheit"
        
        elif i_convention.upper() == "F":
            result = int(round((degree - 32) * 5 / 9))
            o_convention = "Celsius"
        
        else:
            print("Input proper convention.")
            quit()
        
        print("The temperature in", o_convention, "is", result, "degrees.")


    def Length():
        
        
        unit1 = input("Which unit would you like to convert from: ")
        
        unit2 = input("Which unit would you like to convert to: ")
        
        num1 = input("Enter your value: " )
        
        if unit1 == "cm" and unit2 == "m":
            ans = float(num1)/100       
            print(f"Answer Is: {ans}")
        elif unit1 == "mm" and unit2 == "cm":
            ans = float(num1)/10
            print(f"Answer Is: {ans}")
        
        elif unit1 == "m" and unit2 == "cm":
            ans = float(num1)*100
            print(f"Answer Is: {ans}")
        
        elif unit1 == "cm" and unit2 == "mm":
            ans = float(num1)*10
            print(f"Answer Is: {ans}")
        
        elif unit1 == "mm" and unit2 == "m":
            ans = float(num1)/1000
            print(f"Answer Is: {ans}")
        
        elif unit1 == "m" and unit2 == "mm":
            ans = float(num1)*1000
            print(f"Answer Is: {ans}")  
        
        elif unit1 == "km" and unit2 == "m":
            ans = float(num1)*1000
            print(f"Answer Is: {ans}")
        
        elif unit1 == "m" and unit2 == "km":
            ans = float(num1)/1000
            print(f"Answer Is: {ans}")
        
        elif unit1 == "mm" and unit2 == "km":
            ans = float(num1)/1000000
            print(f"Answer Is: {ans}")


    def Weight():
        
        weight = float(input("What is your weight? "))
        
        unit = input("Kgs or Lbs? ")
        
        pound = 2.20462

        kilo = 0.453592
        
        converted_weight = float(weight * pound)
        
        formatted_float = float(weight*kilo)

        print(weight)
        
        print(unit)

        if unit == "Kgs":
            print(f"Your weight is {converted_weight} Lbs")
        
        elif unit == "Lbs":
            print(f"Your weight is {formatted_float} Kgs.")
        
        else:
            print("That is not a valid input. Please try again.")


class Converter:

    print("Available Functions Are: \n=>Temperature\n=>Length\n=>Weight")

    print("Enter 'temp' or 'len' or 'wei' to acess the functions")

    user_input  = input("Choose Your Function: ")

    if user_input == "temp":
        Functions.Temperature()
    
    elif user_input == "len":
        Functions.Length()
    
    elif user_input == "wei":
        Functions.Weight()
    
    else:
        print("ERORR")

Converter()