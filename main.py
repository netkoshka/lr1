from math import sqrt

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

D = b * b - 4 * a * c
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print("Корни:", x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print('Корень:', x)
else:
    print("Корней нет")

