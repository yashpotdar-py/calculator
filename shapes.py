import math


class Dimensions():

    
    def _2d():

        
        print("Shapes Available: (For Perimeter Type 'Quadrilateral' For Any 4 Sided Shapes)\
            \nSquare \nRectangle \nTriangle \nCircle")
        
        shape_choose = input("Choose A Shape: ")
        
        function_choose = input("Type 'peri' for Perimeter\
            Type 'area' for Area\n=>")
        
        
        def Perimeter():
            
            if shape_choose == "Quadrilateral":
                side1 = float(input("Side 1: "))
                side2 = float(input("Side 2: "))
                side3 = float(input("Side 3: "))
                side4 = float(input("Side 4: "))
                perimeter = side1 + side2 + side3 + side4
                print(f"The Perimeter is: {perimeter} units")
                        
            elif shape_choose == "Triangle":
                side1 = float(input("Side 1: "))
                side2 = float(input("Side 2: "))
                side3 = float(input("Side 3: "))
                perimeter = side1 + side2 + side3                
                print(f"The Perimeter is: {perimeter} units" )
            
            elif shape_choose == "Cirlce":
                radius = int(input("Radius: "))
                perimeter = 2 * math.pi * radius
                print(f"The Perimeter is: {perimeter} units" )
        
        
        def Area():
            
            if shape_choose == "Square": 
                side = float(input("Side: "))
                area = side*side
                print(f"Area of Square Is: {area} units^2")

            elif shape_choose == "Rectangle":
                length = float(input("Length: "))
                width = float(input("Width: "))
                area = length * width
                print(f"Area Of Rectangle Is: {area} units^2")
            
            elif shape_choose == "Triangle":
                base = float(input("Base: "))
                height = float(input("Height: "))
                area = 0.5 * base * height
                print(f"Area Of Triangle Is: {area} units^2")

            elif shape_choose == "Cirlce":
                radius = float(input("Radius: "))
                area = math.pi * radius * radius
                print(f"Are Of Circle Is: {area} units^2")

    
        if function_choose == "peri":
            Perimeter()

        elif function_choose == "area":
            Area()
    

    def _3d():
        
        
        print("Shapes Available:\
            \nCube \nCuboid \nSphere")
        
        shape_choose1 = input("Choose A Shape: ")
        
        function_choose1 = input("Type 'area' for Total Surface Area\
            Type 'volume' for Volume\n=>")

        
        def Surface_Area():


            if shape_choose1 == "Cube":
                edge = float(input("Side: "))
                surface_area = 6 * edge * edge
                print(f"Total Surface Area Is: {surface_area} units^2")

            elif shape_choose1 == "Cuboid":
                l = float(input("Length: "))
                b = float(input("Width: "))
                h = float(input("Height: "))
                surface_area = 2 * ((l * b) + (b * h) + (l * h))
                print(f"Total Surface Area Is: {surface_area} units^2")
            
            elif shape_choose1 == "Sphere":
                radius = float(input("Radius: "))
                surface_area = 4 * math.pi * radius * radius
                print(f"Total Surface Area Is: {surface_area} units^2")

        
        def Volume():

            if shape_choose1 == "Cube":
                edge = float(input("Side: "))
                volume = edge * edge * edge
                print(f"Total Surface Area Is: {volume} units^3")

            elif shape_choose1 == "Cuboid":
                l = float(input("Length: "))
                b = float(input("Width: "))
                h = float(input("Height: "))
                volume = l * b * h
                print(f"Total Surface Area Is: {volume} units^3")
            
            elif shape_choose1 == "Sphere":
                radius = float(input("Radius: "))
                volume = (4/3) * math.pi * radius * radius * radius
                print(f"Total Surface Area Is: {volume} units^3")

        
        if function_choose1 == "area":
            Surface_Area()

        elif function_choose1 == "volume":
            Volume()
        
        else:
            print("ERORR")


class Shapes:
    
    dimension = input("**Choose A Shape(2D/3D):")

    if dimension == "2D":
        Dimensions._2d()
    
    elif dimension == "3D":
        Dimensions._3d()

    else:
        print("ERORR")

Shapes()