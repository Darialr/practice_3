x, y = map(int, input('Введите два целых числа: ').split())
print(int(x % y == 0) or int(y % x == 0))
