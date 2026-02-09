import random
import time
import statistics

from heapsort import heapsort


# --------- Quicksort (in-place, random pivot) ----------
def quicksort(a):
    def partition(lo, hi):
        pivot_idx = random.randint(lo, hi)
        a[pivot_idx], a[hi] = a[hi], a[pivot_idx]
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    def qs(lo, hi):
        if lo >= hi:
            return
        p = partition(lo, hi)
        qs(lo, p - 1)
        qs(p + 1, hi)

    if len(a) > 1:
        qs(0, len(a) - 1)


# --------- Merge Sort (returns new list) ----------
def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    return merge(left, right)

def merge(left, right):
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


# --------- Data generators ----------
def gen_sorted(n):
    return list(range(n))

def gen_reverse(n):
    return list(range(n, 0, -1))

def gen_random(n):
    return [random.randint(0, n) for _ in range(n)]


# --------- Timing ----------
def median_time(sort_fn, data, repeats=5):
    times = []
    for _ in range(repeats):
        arr = data[:]
        t0 = time.perf_counter()

        result = sort_fn(arr)

        # mergesort returns new list; others sort in place
        if result is not None:
            arr = result

        # correctness check
        assert arr == sorted(data)

        t1 = time.perf_counter()
        times.append(t1 - t0)
    return statistics.median(times)


def main():
    random.seed(0)

    algorithms = [
        ("Heapsort", lambda arr: heapsort(arr)),
        ("Quicksort", lambda arr: quicksort(arr)),
        ("Mergesort", lambda arr: mergesort(arr)),
        ("Python sort", lambda arr: (arr.sort(), None)[1]),  # in-place
    ]

    distributions = [
        ("sorted", gen_sorted),
        ("reverse", gen_reverse),
        ("random", gen_random),
    ]

    sizes = [1000, 5000, 10000, 20000]

    print("Median runtime (seconds), repeats=5\n")

    for n in sizes:
        print(f"=== n = {n} ===")
        for dist_name, gen in distributions:
            data = gen(n)
            print(f"  [{dist_name}]")
            for algo_name, fn in algorithms:
                t = median_time(fn, data, repeats=5)
                print(f"    {algo_name:12s} {t:.6f}")
        print()

if __name__ == "__main__":
    main()

