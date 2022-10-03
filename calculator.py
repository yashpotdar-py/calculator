#calculator.py
import math

class Opertations():
    
    #basic caclulator
    def basic():
        
        
        try:
            eqaution = input("Enter Your Equation: ")

            result = eval(eqaution)
            print(f"Answer is: {result}")
        except:
            print("MATH ERORR")
    
    
    #complex calculator
    def complex():
        
        
        print("Available Functions are:\
            \n=>Trigonometric Ratios\
            \n=>Factorial\
            \n=>Exponent\
            \n=>Logarithm\
            \n=>Square Root")
        print("Enter Follwing Keywords:\
            \n'trigo' for TRignometry\
            \n'fact' for Factorial\
            \n'expo' for Exponential\
            \n'log' for Logarithm\
            \n'ln' for Natural LOgarithm\
            \n'sqrt' for Square Root")

        #input to choose operation
        userinput = input("Choose Operation:")

        #Trignometric Ratios
        if userinput == "trigo":

            print("Unit is in Radians")
            input1 = input("Enter A Function[sin,cos,tan, etc]: ")

            a = int(input("Choose Your Number: "))
            
            try:
                
                #sin
                if input1 == 'sin':
                    print(f"Answer is: {math.sin(a)}")
                
                #cos
                elif input1 == 'cos':
                    print(f"Answer is: {math.cos(a)}")
                
                #tan
                elif input1 == 'tan':
                    print(f"Answer is: {math.tan(a)}")
                
                #cosec
                elif input1 == 'cosec':
                    print(f"Answer is: {1/math.sin(a)}")
                
                #sec
                elif input1 == 'sec':
                    print(f"Answer is: {1/math.cos(a)}")
                
                #cot
                elif input1 == 'cot':
                    print(f"Answer is: {1/math.tan(a)}")
                
                else:
                    print("ERORR")
            except:
                print("Math ERORR")

        #Factorial(Erorr When -ve or float)
        elif userinput == "fact":
            try:
                input2 = int(input("Choose A Number: "))
                result = math.factorial(input2)
                print(f"Answer is: {result}")
            except:
                print("Math ERORR")
        
        #Power(Exponents)
        elif userinput == "expo":
            try:
                n1 = int(input("Choose Base: "))
                n2 = int(input("Choose Power: "))
                exponent = n1**n2
                print(f"Answer Is: {exponent}")
            except:
                print("Math ERORR")

        #Logarithm
        elif userinput == "log":
            try:
                a = float(input("Choose Your Number: "))
                result = math.log10(a)
                print(f"Answer Is: {result}")
            except:
                print("Math ERORR")

        #Natural Logarithm
        elif userinput == "ln":
            try:
                a = float(input("Choose Your Number: "))
                result = math.log10(a)
                print(f"Answer Is: {result}")
            except:
                print("Math ERORR")

        #Square Root
        elif userinput == "sqrt":
            try:
                a = float(input("Input Number: "))
                result = math.sqrt(a)
                print(f"Answer Is: {result}")
            except:
                print("Math ERORR")


class Calculator():
        
        print("For Basic Calculator, Input \033[1m 'basic' \033[0m \
            For Complex Operations, Input \033[1m 'complex' \033[0m ")
        
        input = input("Enter Your Choice: ")

        if input == "basic":
            Opertations.basic()
        
        elif input == "complex":
            Opertations.complex()

        else:
            print("ERORR")


Calculator()