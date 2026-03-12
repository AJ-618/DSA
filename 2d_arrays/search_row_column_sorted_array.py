"""
Search in a row and column sorted 2d array

i/p: [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
], k = 29

o/p: 2 1

Time Complexity: O(R + C)
"""

def search(arr: list, x: int):
    """Search in a row/column sorted 2d array"""

    row = len(arr)
    col = len(arr[0])

    i = 0
    j = col - 1

    while (i < row and j >= 0):
        if arr[i][j] == x:
            print(f"{x} found at index [{i}][{j}]")
            return

        if arr[i][j] > x:
            j -= 1
        else:
            i += 1

    print(f"{x} not found")


if __name__ == '__main__':
    nums = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]
    ]

    search(nums, 29) # 29 found at index [2][1]
