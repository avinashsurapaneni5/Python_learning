import math

radius = float(input("enter the radius of a circle: "))
# circumference of a circle
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")


# area of a circle

area = math.pi * pow(radius, 2)

print(f"The area of circle is: {round(area, 2)}cm^2")

# Hypotenuse of right angle triangle

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Hypotenuse of right angle triangle : {c}")