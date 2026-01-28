"""
--------- Heap Sort ---------

Basic Idea: Find the max element and then sort it.
The idea is similar to selection sort, but instead
of linear search, heap sort makes use of the 'Max Heap'
data structure. Building a max heap from a random
array is O(n) time. After building the max heap, we
swap the last element with the root of the max. After
that, we perform the heapify operation, because it is
an operation when the subtrees are heapified and
only the root is disturbed.

Heap sort can be mainly seen as an improvement of selection
sort.

Time -> O(nlogn), i.e. the best time complexity we can get in
any comparison based sorting algorithm. In comparison, merge
sort takes O(nlogn) time on worst case, quick sort takes the
same time on average case, but for heap sort, its the same in
every case.

When we compare heap sort with merge sort and quick sort, the
constants hidden in Heap sort algorithm are higher than merge
sort and quick sort. In practice, merge and quick sort takes
less time compared to heap sort. And that is why merge and
quick sort are more popular.

Intro sort is the sorting algorithm used in cpp stdlib. It uses
quick sort but switches to heap sort when recursion depth of the
former goes beyond logn. So heap sort is not used as the main
sorting algorithm in stdlib's but is used as a helper algorithm
in hybrid algorithms.

i/p: [10, 15, 50, 4, 20]
"""

# Helpers ---------------------------------------------------------
def _heapify(arr: list, n: int, i: int):
    "max heapify"

    largest = i # parent of leaf node, considered largest by default
    left = (2 * i) + 1  # left leaf node
    right = (2 * i) + 2 # right leaf node

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        _heapify(arr, n, largest) # to make sure that the child
                                        # is heapified after the swap as well

def _build_heap(arr: list):
    "create max heap required for heap sort"

    n = len(arr)
    leaf_parent_index = int((n - 2) / 2)

    for i in range(leaf_parent_index, -1, -1):
        _heapify(arr, n, i)

# Heap Sort ----------------------------------------
def heap_sort(arr: list):
    "heap sort implementation"

    n = len(arr)

    _build_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)


if __name__ == '__main__':
    nums = [10, 15, 50, 4, 20]
    heap_sort(nums)
    print(nums)
