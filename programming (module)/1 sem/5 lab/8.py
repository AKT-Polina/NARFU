#Лямбда:

lst = [21, 49, 67, 63, 78, 77, -99]
y = lambda i: i %7
for i in lst:
    print(y(i))

#map
def dell(i):
    return i % 7

lst = [21, 49, 67, 63, 78, 77, -99]
new_list = list(map(dell, lst))
print(new_list)

i = input()