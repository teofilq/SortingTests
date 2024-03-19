import sys

sys.setrecursionlimit(1000000000)

def countingSort(L):
    S = [0] * (max(L) + 1)
    for i in L:
        S[i] += 1
    L = []
    for i in range(len(S)):
        L.extend([i] * S[i])
    return L

def partition(L, low, high):
    pivot = L[high]
    i = low - 1
    for j in range(low, high):
        if L[j] <= pivot:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[high] = L[high], L[i + 1]
    return i + 1

def quickSort(L, low, high):
    if low < high:
        pi = partition(L, low, high)
        quickSort(L, low, pi - 1)
        quickSort(L, pi + 1, high)

def shellSort(L, n):
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = L[i]
            j = i
            while j >= gap and L[j - gap] > temp:
                L[j] = L[j - gap]
                j -= gap
            L[j] = temp
        gap //= 2

def margesort(L):
    if len(L) > 1:
        mid = len(L) // 2
        left = L[:mid]
        right = L[mid:]

        margesort(left)
        margesort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                L[k] = left[i]
                i += 1
            else:
                L[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            L[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            L[k] = right[j]
            j += 1
            k += 1

def radix(baza, L):
    maxi = max(L)
    exp = 1
    n = len(L)
    output = [0] * n
    while maxi // exp > 0:
        count = [0] * (baza)
        for i in range(n):
            index = L[i] // exp
            count[index % baza] += 1
        for i in range(1, baza):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = L[i] // exp
            output[count[index % baza] - 1] = L[i]
            count[index % baza] -= 1
            i -= 1
        i = 0
        for i in range(n):
            L[i] = output[i]
        exp *= baza
    return L
