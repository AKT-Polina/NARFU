import random
print(random.randint(0,10000))
print([int(1000*random.random()) for i in range(10)])
list_size = 15
L = list(range(list_size))
print(L)
random.shuffle(L)
print(L)
for list_size in [5, 10, 20, 30]:
  L = list(range(list_size))
  random.shuffle(L)
  print(L)


def mergesort(L):
    if len(L) > 1:
        mid = len(L) // 2
        Left = L[:mid]
        Right = L[mid:]
        mergesort(Left)
        mergesort(Right)
        i = j = k = 0
        while i < len(Left) and j < (Right):
            if Left[i] < Right[j]:
                L[k] = Left[i]
                i += 1
            else:
                L[k] = Right[j]
                j += 1
            k += 1
        while i < len(Left):
            L[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            L[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            L[k] = Right[j]
            j += 1
            k += 1
        return L
    L = [3, 6, 8, 2, 9, 1, 7, 0, 5, 9, 4]
    print(mergesort(L))
