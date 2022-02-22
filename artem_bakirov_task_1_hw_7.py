import math
x = int(input("Введите сторону квадрата:"))
def squre_operation(x: int):
    return 'Периметр = ' + str(x * 4), 'Диагональ = ' + str(round(x * math.sqrt(2), 1)), 'Площадь = ' + str(x * x)


print(squre_operation(x))