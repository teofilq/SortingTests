import sys
import time
import signal

sys.setrecursionlimit(1000000000)

from sorter import counting_sort, quick_sort, shell_sort, merge_sort, radix_sort

def signal_handler(signum, frame):
    raise Exception("The sorting operation exceeded the 2-minute limit.")

signal.signal(signal.SIGALRM, signal_handler)

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
        try:
            signal.alarm(120)  # 120 seconds = 2 minutes
            elements_copy = elements[:]  
            start_time = time.time()
            sorted_elements = sort_function(elements_copy)
            end_time = time.time()
            signal.alarm(0)  
            print(f"Test with N={n}, MAX={maxim}: {end_time - start_time} seconds")
            # Check if correctly sorted
            assert sorted_elements == sorted(elements), "List is not correctly sorted!"
        except Exception as e:
            print(e)
    print(f"{sort_function_name} testing completed.\n")

tests = read_tests('tests.txt')

sort_functions = {
    #'counting_sort': counting_sort,
    #'quick_sort': quick_sort,
    #'shell_sort': shell_sort, 
    #'merge_sort': merge_sort,
    #'radix_sort_b10': lambda L: radix_sort(L, 10),
    'radix_sort_b16': lambda L: radix_sort(L, 2**16),
    #'python_sorted': sorted,
}

for name, function in sort_functions.items():
    test_sort_function(name, function, tests)
