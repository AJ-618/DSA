"""
Find median of a row sorted 2d array

i/p: [
    [2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9],
    [100, 200, 400, 500, 800],
]

o/p: [1, 2, 3, 5, 6, 7, 8, 9, 10, 100, 200, 400, 500, 800] => 8

Time Complexity -> O(row * column)
"""

from itertools import chain

def median_2darray_general(arr: list) -> int:
    """Find median in a 2d row sorted array.
    Note that this is a general solution for
    all 2d arrays regardless of the fact that
    the items in them are row-sorted."""

    flattened_array = list(chain.from_iterable(arr))
    flattened_array.sort()

    median = int(len(flattened_array) / 2)
    return flattened_array[median]


if __name__ == '__main__':
    nums = [
        [2, 4, 6, 8, 10],
        [1, 3, 5, 7, 9],
        [100, 200, 400, 500, 800]
    ]

    print(median_2darray_general(nums))
