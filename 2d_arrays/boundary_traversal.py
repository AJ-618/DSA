"""
Traverse the boundary of an 2d array.

i/p: [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]
]

o/p: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5

Time complexity -> Theta(rows + cols)

NOTE: It is expected that all rows will have the same number of
elements
"""

def boundary(arr: list):
    "Traverse the boundary of a 2d array"

    # dimension -> rows = 4, cols = 4
    rows = len(arr)
    cols = len(arr[0])

    if rows == 1:
        print(*arr[0], sep=' ', end=' ')
    elif cols == 1:
        curr_row = 0
        while curr_row < rows:
            print(arr[curr_row][0], sep=' ', end=' ')
            curr_row += 1
    else:
        # Print 1st row
        print(*arr[0], sep=' ', end=' ')

        # Print rightmost boundary
        for i in range(1, rows - 1):
            print(arr[i][cols - 1], sep=' ', end=' ')

        # Print last row
        print(*reversed(arr[rows - 1]), sep=' ', end=' ')

        # Print leftmost boundary
        for i in range(rows - 2, 0, -1):
            print(arr[i][0], sep=' ', end=' ')

    print()


if __name__ == '__main__':
    arr_2d = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    boundary(arr_2d)

    arr_2d = [
        [11, 12, 13, 14],
        [15, 16, 17, 18]
    ]
    boundary(arr_2d)

    arr_2d = [[10, 20, 30, 40]]
    boundary(arr_2d)

    arr_2d = [
        [11],
        [22],
        [33],
        [44]
    ]
    boundary(arr_2d)
