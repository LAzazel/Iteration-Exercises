'''Итерирование циклами'''

from functools import reduce

def sum_1(*args):
    res = 0
    for i in args:
        res += i
    return res

def sum_2(*args):
    res = 0
    for i in range(len(args)):
        res += args[i]
    return res

def sum_3(*args):
    res = 0
    i = 0
    while i < len(args):
        res += args[i]
        i += 1
    return res

def sum_4(*args):
    res = 0
    i = 0
    if i < len(args):
        while True:
            res += args[i]
            i += 1
            if i >= len(args):
                break
    return res

def sum_5(*args):
    return reduce(lambda x, y: x + y, args)

'''Итерирование по двумерному массиву'''

def my_max(x):
    return max([max(i) for i in x])

'''Итерирование объектов-справочников'''

def len_of_life(x):
    res = {}
    for i, j in x.items():
        res[i] = j['died'] - j['born']
    return res



a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
persons = {
    'lenin': { 'born': 1870, 'died': 1924 },
    'mao': { 'born': 1893, 'died': 1976 },
    'gandhi': { 'born': 1869, 'died': 1948 },
    'hirohito': { 'born': 1901, 'died': 1989 },
}


print(sum_1(1, 2, 3, 4, 5, 6))
print(sum_2(1, 2, 3, 4, 5, 6))
print(sum_3(1, 2, 3, 4, 5, 6))
print(sum_4(1, 2, 3, 4, 5, 6))
print(sum_5(1, 2, 3, 4, 5, 6))
print(my_max(a))
print(persons.items())