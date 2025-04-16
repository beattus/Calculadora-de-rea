#AREACALCULATOR

area = 0
length = 0
width = 0
height = 0
base = 0
radius = 0

class main:
    def welcome():
        print("Welcome to the Area Calculator!")
        print("This program will calculate the area of a rectangle, triangle, or circle.")
        print("Please choose one of the following options:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Square")
        print("5. Quit")

    def rectangle():
        global length, width, area
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is {area} square units.")
        return area

    def triangle():
        global base, height, area
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is {area} square units.")
        return area

    def circle():
        global radius, area
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14 * radius ** 2
        print(f"The area of the circle is {area} square units.")
        return area

    def square():
        global length, area
        radius = float(input("Enter the length of the square: "))
        area = length ** 2
        print(f"The area of the square is {area} square units.")
        return area



welcome = main.welcome()
choose = int(input("Enter your choice (1-5): "))
if choose == 1:
    main.rectangle()
elif choose == 2:
    main.triangle()
elif choose == 3:
    main.circle()
elif choose == 4:
    main.square()
elif choose == 5:
    print("Thank you for using the Area Calculator!")
else:
    print("Invalid choice.")