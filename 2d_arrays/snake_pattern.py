"""
Print a 2d Matrix in snake pattern

i/p: [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[10, 11, 12]
]

o/p: 1 2 3 6 5 4 7 8 9 12 11 10
"""

def snake(arr: list):
    "print arr in snake pattern"
    for index, row in enumerate(arr):
        if index % 2 == 0:
            print(*row, sep=' ', end=' ')
        else:
            print(*reversed(row), sep=' ', end=' ')


if __name__ == '__main__':
    two_d_arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]

    snake(two_d_arr)
