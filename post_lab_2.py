#Question 1
print("Enter measurements for rectangle:")
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("Area =", area)
print("Perimeter =", perimeter)

#Question 2
num = int(input("Enter a number: "))
if num==0:
    print("Neither even nor odd")
elif num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#Question 3
side = float(input("Enter side of cube: "))
surfaceArea = 6*(side**2)
vol = side**3
print("Surface Area =", surfaceArea)
print("Volume =", vol)

#Question 4
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = (x + y)*(x - y)   
print("z =", z)

#Question 5
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = (x + y)*(x + y) - 2*x*y
print("z =", z) ## Here z = x^2 + y^2

#Question 6
cel = float(input("Enter temperature in Celsius: "))
fahrenheit = (cel * 9/5) + 32
print(cel, "degree Celcius =", fahrenheit, "degree FarenheitS")