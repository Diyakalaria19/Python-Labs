#Question 1
# import math
# degree = float(input("Enter degrees: "))
# radian = math.radians(degree)   
# print(f"{degree} = {radian} radians")

#Question 2
# import math
# x = float(input("Enter value of x: "))
# y = 6*(x**2) + 4*math.sin(x)
# print("y =",y)

#Question 3
import math
def functions(x):
    f = math.cos(2*x)
    f1 = -2 * math.sin(2*x)
    f2 = -4 * math.cos(2*x)
    return f, f1, f2
x = math.pi
f_result, f1_result, f2_result = functions(x)

print("f(x) =",f_result)
print("f'(x) =",f1_result)
print("f''(x) =",f2_result)
