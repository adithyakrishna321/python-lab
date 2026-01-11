
area_square = lambda side: side ** 2


area_rectangle = lambda length, width: length * width


area_triangle = lambda base, height: 0.5 * base * height


side = float(input("Enter the side of the square: "))
print(f"Area of square: {area_square(side)}")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print(f"Area of rectangle: {area_rectangle(length, width)}")

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
print(f"Area of triangle: {area_triangle(base, height)}")
