import sys
import time
#nr recursiuni
sys.setrecursionlimit(1000000000)
#adaugam functiile de sortare
from sorter import countingSort, quickSort, shellSort, margesort, radix

def read_tests(filename):
    tests = []
    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break  
            n = int(line.strip())
            maxim = int(file.readline().strip())
            elements = list(map(int, file.readline().strip().split()))
            tests.append((n, maxim, elements))
    return tests

def test_sort_function(sort_function_name, sort_function, tests):
    print(f"Testing {sort_function_name}...")
    for n, maxim, elements in tests:
        elements_copy = elements[:] # Copiem lista pentru a nu o modifica
        start_time = time.time()
        if sort_function_name == 'quickSort':
            sort_function(elements_copy, 0, len(elements_copy) - 1)
        else:
            elements_copy = sort_function(elements_copy)  # Alte sortări
        end_time = time.time()
        print(f"Test cu N={n}, MAXIM={maxim}: {end_time - start_time} secunde")
        # Verificăm dacă lista este corect sortată
        assert elements_copy == sorted(elements), "Lista nu este corect sortată!"
    print(f"{sort_function_name} testing completed.\n")

tests = read_tests('tests.txt')

# Dicționar de funcții de sortare pentru a simplifica apelurile
sort_functions = {
    # 'countingSort': countingSort,
     'quickSort': quickSort,
    #'shellSort': lambda L: shellSort(L, len(L)), 
    #'margesort': margesort,
    # 'radix (baza 10)': lambda L: radix(10, L),
    # 'radix (2**16)': lambda L: radix(2**16, L),
    # 'pythonSorted': sorted, 
}


for name, function in sort_functions.items():
    test_sort_function(name, function, tests)
