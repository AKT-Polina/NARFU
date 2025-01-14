def insertion_sort(L):
    n = len(L)
    for i in range(1, n):
        key = L[i]
        j = i - 1
        while j >= 0 and key < L[j]:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key


L = [3, 6, 8, 2, 9, 1, 7, 0, 5, 9, 4]
print("Исходный массив:", L)
insertion_sort(L)
]print("Отсортированный массив:", L)
