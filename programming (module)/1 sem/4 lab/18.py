nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

n1 = []

n2 = []
for i in nums:
    if i % 2 == 0:
        n1.append(i * i)
    else:
        n2.append(i + 2)

print("Четные числа\n", n1)
print("Нечётные числа\n", n2)

i = input()