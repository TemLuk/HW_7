number = int(input('Введите номер месяца: '))

if number in [1, 2, 12]:
    print('Сейчас зима!')
if number in [3, 4, 5]:
    print('Сейчас весна!')
if number in [6, 7, 8]:
    print('Сейчас лето!')
if number in [9, 10, 11]:
    print('Сейчас осень!')
