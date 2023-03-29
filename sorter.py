import random
import time
import sys
sys.setrecursionlimit(100000000)
def countingSort(L):
	S = []
	for i in range(max(L)+1):
		S.append(0)
	for i in L:
		S[i]=S[i]+1
	L=[]
	for i in range(len(S)):
		while S[i]:
			L.append(i)
			S[i]=S[i]-1
	return L


def partition(L, low, high):
  pivot = L[high]
  i = low - 1
  for j in range(low, high):
    if L[j] <= pivot:
      i = i + 1
      (L[i], L[j]) = (L[j], L[i])
  (L[i + 1], L[high]) = (L[high], L[i + 1])
  return i + 1
def quickSort(L, low, high):
  if low < high:
    pi = partition(L, low, high)
    quickSort(L, low, pi - 1)
    quickSort(L, pi + 1, high)

def shellSort(L, n):
    mij = n // 2
    while mij > 0:
        j = mij
        while j < n:
            i = j - mij
            while i >= 0:
                if L[i + mij] > L[i]:
                    break
                else:
                    L[i + mij], L[i] = L[i], L[i + mij]
                i = i - mij
            j += 1
        mij = mij // 2

def margesort(L):
    if len(L)>1:
        mij = len(L)//2
        dr = L[mij:]
        st = L[:mij]
        margesort(dr)
        margesort(st)
        i = j = k = 0
        while i < len(st) and j < len(dr):
            if st[i] <= dr[j]:
                L[k] = st[i]
                i += 1
            else:
                L[k] = dr[j]
                j += 1
            k += 1
        while i < len(st):
            L[k] = st[i]
            i += 1
            k += 1
        while j < len(dr):
            L[k] = dr[j]
            j += 1
            k += 1
    else: return
def radix(baza, L):
    maxi = max(L)
    notsorted=0
    while maxi:
        maxi=maxi//baza
        notsorted=notsorted+1
    Bucket = []
    for i in range(baza):
        Bucket.append([])
    contor=0
    while notsorted:
        for i in range(baza):
            Bucket[i].clear()
        for elem in L:
            z=elem
            z=z//(baza**contor)
            c=z % baza
            Bucket[c].append(elem)
        contor=contor+1
        L.clear()

        for i in range(baza):
            while Bucket[i]:
                L.append(Bucket[i].pop(0))
        notsorted = notsorted-1
    return L
L=[]
S=[]
numere=int(input("introdu cate numere din intervalul 0, 99999 va avea lista de sortat: "))
for i in range(numere):
    S.append(random.randint(0,100000))

print("test și timp raxis sort baza 10: ")
L=S
start = time.time()
radix(10, L)
stop = time.time()
if(L == sorted(L)):
    print('da')
else:
    print('nu')
print(stop-start)

print("test și timp raxis sort baza 2^16: ")
L=S
start = time.time()
radix(65536, L)
stop = time.time()
if(L == sorted(L)):
    print('da')
else:
    print('nu')
print(stop-start)

print("test și timp quicksort: ")
L=S
start = time.time()
quickSort(L, 0, len(L)-1)
stop = time.time()
if(L == sorted(L)):
    print('da')
else:
    print('nu')
print(stop-start)

print("test și timp countingsort: ")
L=S
start = time.time()
countingSort(L)
stop = time.time()
if(L == sorted(L)):
    print('da')
else:
    print('nu')
print(stop-start)

print("test și timp margesort: ")
L=S
start = time.time()
margesort(L)
stop = time.time()
if(L == sorted(L)):
    print('da')
else:
    print('nu')
print(stop-start)

print("test și timp shellsort: ")
L=S
start = time.time()
shellSort(L, numere)
stop = time.time()
if(L == sorted(L)):
    print('da')
else:
    print('nu')
print(stop-start)
