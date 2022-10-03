#main.py

print("Which Program do You Wish to use?")

user_input = input("Enter calc or conv or shapes:")

if user_input == "calc":
    
    from calculator import Calculator
    Calculator()

elif user_input == "conv":
    
    from converter import Converter
    Converter()

elif user_input == "shapes":
    
    from shapes import Shapes
    Shapes()

else:

    quit()