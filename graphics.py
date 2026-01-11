import  Graphics
from Graphics import circle,Rectangle
from Graphics.threedgraphics import cuboid, sphere
from Graphics.circle import *
rad1 = float(input("Enter the radius of the circle:"))
print("Area of circle is: ", circle.area_circle(rad1))
print("Perimeter of circle is :", circle.perimeter_circle(rad1))
len1 = float(input("Enter the length of the Rectacngle:"))
breadth1 = float(input("Enter the breadth of the rectangle:"))
print("Area of rectangle is:",Rectangle.area_rec(len1,breadth1))
print("Perimeter of rectangle is :", Rectangle.perimeter_rec(len1, breadth1))
len2 = float(input("Enter the length of the cuboid:"))
breadth2 = float(input("Enter the breadth of the cuboid:"))
height = float(input("Enter the height of the cuboid:"))
print("Area of cuboid is:", cuboid.area_cuboid(len2, breadth2, height))
print("Perimeter of cuboid is:", cuboid.perimeter_cuboid(len2, breadth2, height))
rad2 = float(input("Enter the radius of the sphere:"))
print("Area of sphere is:", sphere.area_sphere(rad2))
print("Perimeter of sphere is :", sphere.perimeter_sphere(rad2))





from math import pi
def area_circle(radius):
    return pi*radius*radius
def perimeter_circle(radius):
    return 2*pi*radius




def area_rec(length,width):
    return length*width
def perimeter_rec(length,width):
    return 2*(length+width)



def area_cuboid(l,b,h):
    return 2*(l*b+b*h+l*h)
def perimeter_cuboid(l,b,h):
    return 4*(l+b+h)