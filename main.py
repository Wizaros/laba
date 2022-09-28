import math
a = float(input())
b = float(input())
c = float(input())

dis = b**2 - 4 * a * c

if dis >= 0:
    x1 = (-b + math.sqrt(dis)) / (2 * a)
    x2 = (-b - math.sqrt(dis)) / (2 * a)
    print(x1,x2)
else:
    print('Корней нет')