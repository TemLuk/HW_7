# list comprehension
my_nums = [x for x in range(10)]
print(my_nums)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_list = [x for x in fruits if "a" in x]
print(fruits_list)
squares = [x ** 2 for x in range(10)]
print(squares)
even = [x for x in range(10) if x % 2 == 0]
print(even)
numbers = [x ** 2 if x % 2 != 0 else x ** 4 for x in range(10)]
print(numbers)
# dict comprehension
dict1 = dict([(key, value) for (key, value) in zip([1, 2, 3], ['a', 'b', 'c'])])
print(dict1)
dict2 = {num: num ** 2 for num in range(1, 11)}
print(dict2)
r1 = {'IOS': '15.4', 'IP': '10.255.0.1', 'hostname': 'london_r1', 'location': '21 New Globe Walk', 'model': '4451',
      'vendor': 'Cisco'}
dict3 = {key.lower(): value for key, value in r1.items()}
print(dict3)
dict4 = {k: v * 2 for (k, v) in dict1.items()}
print(dict4)
dict5 = {n: n ** 2 for n in range(7) if n % 2 == 0}
print(dict5)
# set comprehension
set1 = {x for x in range(10)}
print(set1)
set2 = {x for x in ['Bob', 'Mark', 'Michail', 'Oleg', 'Mark', ]}
print(set2)
set3 = {(m, n) for n in range(2) for m in range(3, 5)}
print(set3)
set4 = {"apple", "banana", "cherry", 'lime', 'milk', "kiwi", "banana"}
print(set4)
set5 = {n ** 2 for n in range(7) if n % 2 == 0}
print(set5)