"""
Spiral Traversal of a 2d Matrix

i/p: [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

Solution: use 4 pointers i.e. top, right, bottom and left and
increment/decrement them accordingly as we traverse the array.

o/p: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Time complexity -> Theta(row * column)
"""

def spiral_traversal(arr: list):
    "Traverse a 2d matrix spirally"

    row = len(arr)
    col = len(arr[0])

    top = 0
    left = 0
    bottom = row - 1
    right = col - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(arr[top][i], sep=" ", end=" ")
        top += 1

        for i in range(top, bottom + 1):
            print(arr[i][right], sep=" ", end=" ")
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(arr[bottom][i], sep=" ", end=" ")
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(arr[i][left], sep=" ", end=" ")
            left += 1


if __name__ == '__main__':
    nums = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    spiral_traversal(nums)
