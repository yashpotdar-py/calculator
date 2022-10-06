import math


class dimensions:

    @staticmethod
    def second():
        print("**Shapes Available:\n->Square\n->Rectangle\n->Triangle\n->Circle\n**")
        shape_choose = input("Choose a Shape: ")
        shape_choose = shape_choose.lower()

        if shape_choose == 'square':
            try:
                side = float(input("Enter the edge length: "))
                perimeter = side * 4
                area = side ** 2
                print(f"Perimeter of the Square is \033[1m\033[92m{perimeter}\033[0m units\
                    \nArea of the Square is \033[1m\033[92m{area}\033[0m units^2")
            except ValueError:
                print("Enter A Valid Number")
                quit()

        elif shape_choose == 'rectangle':
            try:
                length = float(input("Enter the length: "))
                breadth = float(input("Enter the breadth: "))
                perimeter = 2 * (length * breadth)
                area = length * breadth
                print(f"Perimeter of the Rectangle is \033[1m\033[92m{perimeter}\033[0m units\
                    \nArea of the Rectangle is \033[1m\033[92m{area}\033[0m units^2")
            except ValueError:
                print("Enter A Valid Number")
                quit()

        elif shape_choose == 'triangle':
            try:
                a = float(input("Enter the length of first side: "))
                b = float(input("Enter the length of second side: "))
                c = float(input("Enter the length of third side: "))
                perimeter = a + b + c
                s = perimeter / 2
                heron = s * (s - a) * (s - b) * (s - c)
                area = math.sqrt(heron)
                print(f"Perimeter of the Triangle is \033[1m\033[92m{perimeter}\033[0m units\
                    \nArea of the Triangle is \033[1m\033[92m{area}\033[0m units^2")
            except ValueError:
                print("Enter A Valid Number")
                quit()

        elif shape_choose == 'circle':
            try:
                radius = float(input("Enter the Radius: "))
                perimeter = 2 * math.pi * radius
                area = math.pi * radius * radius
                print(f"Perimeter of the Rectangle is \033[1m{perimeter}\033[0m units\
                    \nArea of the Rectangle is \033[1m{area}\033[0m units^2")
            except ValueError:
                print("Enter A Valid Number")
                quit()

        else:
            print("Error")

    @staticmethod
    def third():
        print("**Shapes Available:\n->Cube\n->Cuboid\n->Sphere\n**")
        shape_choose = input("Choose a Shape: ")
        shape_choose = shape_choose.lower()

        if shape_choose == 'cube':
            try:
                side = float(input("Enter the edge length: "))
                tsa = side * 6
                volume = side ** 3
                print(f"Total Surface Area of the Cube is \033[1m\033[92m{tsa}\033[0m units^2\
                    \nVolume of the Cube is \033[1m\033[92m{volume}\033[0m units^3")
            except ValueError:
                print("Enter A Valid Number")
                quit()

        elif shape_choose == 'cuboid':
            try:
                length = float(input("Enter the length: "))
                breadth = float(input("Enter the breadth: "))
                height = float(input("Enter the height: "))
                lsa = 2 * ((length * height) + (breadth * height))
                tsa = 2 * ((length * breadth) + (breadth * height) + (length * height))
                volume = length * breadth * height
                print(f"Lateral Surface Area of the Cuboid is \033[1m\033[92m{lsa}\033[0m units^2\
                    \nTotal Surface Area of the Rectangle is \033[1m\033[92m{tsa}\033[0m units^2\
                    \nArea of the Rectangle is \033[1m\033[92m{volume}\033[0m units^3")
            except ValueError:
                print("Enter A Valid Number")
                quit()

        elif shape_choose == 'sphere':
            try:
                radius = float(input("Enter the Radius: "))
                tsa = 2 * math.pi * radius
                volume = math.pi * radius * radius
                print(f"Surface Area of the Sphere is \033[1m\033[92m{tsa}\033[0m units\
                    \nVolume of the Sphere is \033[1m\033[92m{volume}\033[0m units^2")
            except ValueError:
                print("Enter A Valid Number")
                quit()

        else:
            print("Error")


class shape:
    dimension_choose = input("**Choose A Dimension(2D/3D): ")
    dimension_choose = dimension_choose.lower()

    if dimension_choose == '2d':
        dimensions.second()

    elif dimension_choose == '3d':
        dimensions.third()

    else:
        print("Error")
