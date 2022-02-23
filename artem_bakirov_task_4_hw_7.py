def word(x):
    return x == x[::-1]


x = input('Введите слово: ')
print(word(x))
