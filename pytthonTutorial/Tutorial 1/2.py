from math import *

def areaperimeter(radius):
    area=pi*radius**2
    perimeter=2*pi*radius
    return f"area is: {area:.2f} & perimeter is: {perimeter:.2f}"

radius=int(input("Enter the radius of the circle: "))
result=areaperimeter(radius)
print(result)