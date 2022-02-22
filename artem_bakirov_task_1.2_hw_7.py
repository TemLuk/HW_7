def fun1(x: int):
    pass


print(fun1(45))


def fun2(x, y):
    return x + y


print(fun2(-5, 10))


def fun3(n: int):
    def fun4(m: int):
        return n * m

    return fun4(4)


new = fun3(50)
print(new)


def fun5(a, b, c=2):
    return a + b * c


print(fun5(2, 3))


def fun6(a, *args):
    return a, args


print(fun6(1, 2, 3))


def fun7(**kwargs):
    return kwargs


print(fun7(key='value', value='key'))

