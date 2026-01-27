import random
import time
from quicksort import randomized_quicksort, deterministic_quicksort

def test_sort(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    end = time.time()
    return end - start

sizes = [100, 200, 500]

for n in sizes:
    arr = list(range(n))

    t1 = test_sort(randomized_quicksort, arr)
    t2 = test_sort(deterministic_quicksort, arr)

    print(f"Size {n}:")
    print(f"  Randomized Quicksort: {t1:.6f} seconds")
    print(f"  Deterministic Quicksort: {t2:.6f} seconds")
    print()
