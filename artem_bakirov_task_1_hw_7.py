import math
x = float(input("Введите сторону квадрата:"))
def squre_operation(x: float):
    return 'Периметр = ' + str(x * 4), 'Диагональ = ' + str(round(x * math.sqrt(2), 1)), 'Площадь = ' + str(x * x)


print(squre_operation(x))
