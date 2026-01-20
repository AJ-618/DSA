"""
-------- Quick Sort Introduction ---------

1. Divide and Conquer Algorithm
2. Worst case Time complexity -> O(n^2)
3. Despite O(n^2) worst case, it is considered
   faster, because of the following reasons.
   a. In-place
   b. Cache friendly
   c. Average case is O(nlogn)
   d. Tail recursive
4. Partition is the key function (Naive, Lomuto, Hoare)
   Quick sort is stable when we use Naive partition algorithm.
5. If we don't need stability, quick sort is actually the
   fastest algorithm which is used in libraries also. But
   if stability is required, then merge sort is preferred.
6. In general, a random pivot is selected when implementing
   the algorithm in a standard library function. This is so
   because if the array is already sorted and we use quick
   sort, then we get the worst time complexity i.e. O(n^2),
   but by selecting the pivot at random, we normalize it.
   NOTE: Worst time complexity is when the partition is done
   in the following way: [x1, x2,.....xn] -> [x1], [x2...xn].
"""

def lomuto(arr: list, low: int, high: int) -> int:
    """Lomuto partition"""

    # Helper ---------------------------------------
    def swap(arr: list, x: int, y: int):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp

    # Lomuto ---------------------------------------
    pos = low - 1

    for i in range(low, high):
        if arr[i] < arr[high]:
            pos += 1
            swap(arr, i, pos)

    pos += 1
    swap(arr, pos, high)

    return pos


def hoare(arr: list, low: int, high: int):
    "Hoare partition implementation"
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        # Move i to the right; stops when it finds an element >= pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move j to the left; stops when it finds an element <= pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers cross, return the split point
        if i >= j:
            return j

        # Swap the elements to put them on the correct sides
        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr: list, low: int, high: int, partition: str='hoare'):
    "Quick sort"
    if low < high:
        if partition == 'hoare':
            p = hoare(arr, low, high)
            quick_sort(arr, low, p)
            quick_sort(arr, p + 1, high)
        else:
            p = lomuto(arr, low, high)
            quick_sort(arr, low, p - 1)
            quick_sort(arr, p + 1, high)


if __name__ == '__main__':
    nums = [8, 4, 7, 9, 3, 10, 5]
    quick_sort(nums, 0, len(nums) - 1, 'lomuto')
    print(nums)
