word = input('Введите слово: ')
if word == word[::-1]:
    print(True)
elif word != word[::-1]:
    print(False)
