# Assignment 4 Report — Heaps and Priority Queues

## 1) Heapsort Implementation
I implemented Heapsort in Python using a max-heap stored in a list (array).
The algorithm works by first building a max-heap, where the largest element
is always at the root. The maximum element is then repeatedly removed and
placed at the end of the list until the list is fully sorted.

## 2) Heapsort Time Complexity
Heapsort runs in O(n log n) time in the best, average, and worst cases.

This is because building the heap takes O(n) time, and then the algorithm
performs n extractions. Each extraction requires a sift-down operation that
takes O(log n) time.

## 3) Heapsort Space Complexity
Heapsort sorts the array in place and uses only a constant amount of extra
memory, so its space complexity is O(1).

## 4) Empirical Comparison with Other Sorting Algorithms
Heapsort was compared with Quicksort, Merge Sort, and Python’s built-in
sorting algorithm using different input sizes and data distributions such as
sorted, reverse-sorted, and random lists.

### Results

=== n = 1000 ===
  [sorted]
    Heapsort     0.001842
    Quicksort    0.001777
    Mergesort    0.001490
    Python sort  0.000013
  [reverse]
    Heapsort     0.001726
    Quicksort    0.001771
    Mergesort    0.001982
    Python sort  0.000014
  [random]
    Heapsort     0.002576
    Quicksort    0.002428
    Mergesort    0.002481
    Python sort  0.000171

=== n = 5000 ===
  [sorted]
    Heapsort     0.012293
    Quicksort    0.008762
    Mergesort    0.007449
    Python sort  0.000059
  [reverse]
    Heapsort     0.011356
    Quicksort    0.007903
    Mergesort    0.008905
    Python sort  0.000096
  [random]
    Heapsort     0.017716
    Quicksort    0.010660
    Mergesort    0.016117
    Python sort  0.001873

=== n = 10000 ===
  [sorted]
    Heapsort     0.025843
    Quicksort    0.019541
    Mergesort    0.016854
    Python sort  0.000115
  [reverse]
    Heapsort     0.026106
    Quicksort    0.018785
    Mergesort    0.017661
    Python sort  0.000153
  [random]
    Heapsort     0.025736
    Quicksort    0.024133
    Python sort  0.003955

=== n = 20000 ===
  [sorted]
    Heapsort     0.069259
    Quicksort    0.039562
    Mergesort    0.047845
    Python sort  0.000263
  [reverse]
    Heapsort     0.059156
    Quicksort    0.040336
    Mergesort    0.038279
    Python sort  0.000269
  [random]
    Heapsort     0.081656
    Quicksort    0.051025
    Mergesort    0.073621
    Python sort  0.010864



### Discussion
The benchmark results show that Heapsort consistently follows O(n log n) behavior
across all input distributions. Its performance does not significantly change for
sorted, reverse-sorted, or random inputs, which matches theoretical analysis.

Quicksort generally performed faster than Heapsort on random input due to lower
constant factors, but its performance depends on pivot selection. Merge Sort
maintained O(n log n) behavior but required additional memory.

Python’s built-in sort was the fastest in all cases because it is implemented in C
and uses Timsort, which is highly optimized and adaptive to existing order.


## 5) Priority Queue Design
The priority queue was implemented using a binary max-heap stored in a list.
A max-heap was chosen so that the highest priority task is always processed
first.

## 6) Priority Queue Operations and Complexity
The following operations were implemented:
- is_empty(): O(1)
- insert(task): O(log n)
- extract_max(): O(log n)
- increase_key(): O(log n)
- decrease_key(): O(log n)

A dictionary mapping task IDs to heap indices was used to allow priority
updates in constant time.
