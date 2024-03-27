import sys

sys.setrecursionlimit(1000000000)

def counting_sort(L):
    if not L:  
        return L
    S = [0] * (max(L) + 1)
    for i in L:
        S[i] += 1
    L[:] = []  
    for i in range(len(S)):
        L.extend([i] * S[i])
    return L

def quick_sort(L):
    def median_of_five(arr, low, high):
        mid = low + (high - low) // 2
        quarter = low + (high - low) // 4
        three_quarters = low + 3 * (high - low) // 4

        points = [low, quarter, mid, three_quarters, high]
        values = [arr[i] for i in points]
        sorted_indices = [x for _, x in sorted(zip(values, points))]

        median_index = sorted_indices[2]

        return median_index

    def partition(arr, low, high):
        pivot_index = median_of_five(arr, low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def iterative_quick_sort(arr):
        stack = [(0, len(arr) - 1)]
        while stack:
            start, end = stack.pop()
            if start < end:
                pi = partition(arr, start, end)
                stack.append((start, pi - 1))
                stack.append((pi + 1, end))

    iterative_quick_sort(L)
    return L

def shell_sort(L):
    n = len(L)
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
    return L

def merge_sort(L):
    def merge(left, right, arr):
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    if len(L) > 1:
        mid = len(L) // 2
        left = L[:mid]
        right = L[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, L)
    return L

def radix_sort(L, base=10):
    if not L:
        return L
    maxi = max(L)
    exp = 1
    while maxi // exp > 0:
        output = [0] * len(L)
        count = [0] * base
        for i in L:
            index = (i // exp) % base
            count[index] += 1
        for i in range(1, base):
            count[i] += count[i - 1]
        i = len(L) - 1
        while i >= 0:
            index = (L[i] // exp) % base
            output[count[index] - 1] = L[i]
            count[index] -= 1
            i -= 1
        for i in range(len(L)):
            L[i] = output[i]
        exp *= base
    return L
