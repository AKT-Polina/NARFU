def func(a):
    min = a[0]
    for i in a:
        if i < min:
            min = i
    max = a[0]
    for i in a:
        if i > max:
            max = i
    print(max, min)

def func (*args):
    min = args[0]
    for i in args:
        if i < min:
            min = i
    max = args[0]
    for i in args:
        if i > max:
            max = i
    print(max, min)

lst = [1, 2, 3, 6, 7, 93, -9]
func(lst)