lst = [21, 49, 67, 63, 78, 77, -99]

a = list(filter(lambda x: x % 7 == 0, lst))
print(a)