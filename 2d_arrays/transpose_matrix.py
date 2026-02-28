"""
Transpose a 2d matrix with n * n dimensions

i/p: [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

o/p: [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

Time & Space complexity -> O(n * n)

NOTE: We are updating the matrix in-place and not using any auxillary one
so the number of rows and columns are equal
"""

def transpose(arr: list) -> list:
    "Transpose a 2d matrix"

    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


if __name__ == '__main__':
    nums = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    transpose(nums)
    print(nums)
