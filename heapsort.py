def sift_down(a, start, end):
    root = start
    while True:
        left = 2 * root + 1
        if left >= end:
            break

        right = left + 1
        child = left

        if right < end and a[right] > a[left]:
            child = right

        if a[child] > a[root]:
            a[root], a[child] = a[child], a[root]
            root = child
        else:
            break


def heapify(a):
    n = len(a)
    for i in range((n - 2) // 2, -1, -1):
        sift_down(a, i, n)


def heapsort(a):
    heapify(a)
    for end in range(len(a) - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end)
    return a


# quick test
nums = [5, 1, 9, 3, 7]
print(heapsort(nums))
