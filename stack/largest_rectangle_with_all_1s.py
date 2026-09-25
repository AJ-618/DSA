"""
Find the largest rectangle with all 1s.

i/p: [1, 0, 0, 1, 1]
     [0, 0, 0, 1, 1]
     [1, 1, 1, 1, 1]
     [0, 1, 1, 1, 1]
"""

def largest_consecutive_ones(mat: list, row: int) -> int:
    cols = len(mat[0])

    res = 0

    for i in range(cols - 1, -1, -1):
        if mat[row][i] == 0:
            break
        res += mat[row][i]

    return res

def max_rectangle(mat: list[list[int]]):
    res = largest_consecutive_ones(mat, row=0)

    rows = len(mat)
    cols = len(mat[0])

    for i in range(1, rows):
        for j in range(0, cols):
            if mat[i][j] == 1:
                mat[i][j] += mat[i - 1][j]

        res = max(res, largest_consecutive_ones(mat, i))

    return res

if __name__ == '__main__':
    arr1 = [
     [1, 0, 0, 1, 1],
     [0, 0, 0, 1, 1],
     [1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1],
    ]

    print(max_rectangle(arr1))
