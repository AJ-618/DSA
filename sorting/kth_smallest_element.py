"""
----------------- Find K'th smallest element in the array -----------------

i/p: [10, 4, 5, 8, 11, 6, 26], k = 5
o/p: 10

Basic Idea: partition the array using the pivot, then move either to the left
or right depending if the index of the pivot is smaller or greater than K. When
pivot's index == K, then we return.

NOTE: Lomuto partition is being used, thus function not optimal if we want less
memory writes. Use hoare for that case. 

Time Complexity on Average -> O(nlogn)
"""

def partition(arr: list, low: int, high: int) -> int:
    "Find pivot - Lomuto"

    def _swap(arr: list, x: int, y: int):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp

    pos = low - 1
    pivot = arr[high]

    for i in range(low, high):
        if arr[i] < pivot:
            pos += 1
            _swap(arr, i, pos)

    pos += 1
    _swap(arr, pos, high)

    return pos


def find(arr: list, k: int) -> int:
    "Find K'th largest element"

    low = 0
    high = len(arr) - 1

    while low <= high:
        pivot = partition(arr, low, high)
        print(pivot, arr)

        if pivot == k - 1:
            return arr[pivot]

        if pivot < k - 1:
            low = pivot + 1
        else:
            high = pivot - 1

    return -1


if __name__ == '__main__':
    nums = [10, 4, 5, 8, 11, 6, 26]
    print(find(nums, 5))    # 10
