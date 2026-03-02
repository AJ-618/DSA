"""
Rotate matrix anti-clockwise by 90 degrees

i/p: [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

o/p: [
    [3, 6, 9],
    [2, 5, 8],
    [1, 4, 7]
]

Solution = Transpose + Reverse (No Aux space required, in-place solution)

Time complexity -> Theta(n)
Space complexity -> Theta(1)

NOTE: We are rotating a 2d array anti-clockwise with dimensions n * n
"""

def rotate_90(arr: list):
    "rotate a 2d array anti-clockwise by 90 degrees"

    n = len(arr)

    # Transpose the 2d matrix
    for i in range(n):
        for j in range(i + 1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # Reverse the columns to rotate the transposed matrix anti-clockwise
    # by 90 degrees
    for i in range(n):
        low = 0
        high = n - 1
        while low < high:
            arr[low][i], arr[high][i] = arr[high][i], arr[low][i]
            low += 1
            high -= 1


if __name__ == '__main__':
    nums = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_90(nums)
    print(nums)
