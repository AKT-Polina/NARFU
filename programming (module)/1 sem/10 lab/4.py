def insertionsort(L):                     # функция сортировки методом вставок
  for i in range(1, len(L)):
        key = L[i]
        j = i - 1
        while j >= 0 and key < L[j]:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key
  sorted=L
  return sorted

def mergesort(L):                         # функция сортировки методом слияния
 if len(L) > 1:
        mid = len(L) // 2
        Left = L[:mid]
        Right = L[mid:]
        mergesort(Left)
        mergesort(Right)
        i = j = k = 0
        while i < len(Left) and j < len(Right):
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
            L[k] = Right[j]
            j += 1
            k += 1
        return L
  
L1 = [3,7,8,2,9,1,7,0,5,9,4]
L2 = [3,6,8,2,9,1,7,0,5,9,4]
assert insertionsort(L1) == mergesort(L2)


