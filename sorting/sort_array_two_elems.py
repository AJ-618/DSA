"""
-------- Sort an Array with two types of Elements --------

i/p: [-12, 18, 10, -15]
o/p: [-12, -15, 10, 18]

Problem: We have to sort an array with +ve as well as -ve
integers as well.

Approach: Use classic Hoare's partition.

Time -> Theta(n), Space -> Theta(1)
"""

def hoare(arr: list):
    "Hoare two elem type implementation"

    def _swap(arr: list, x: int, y: int):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp

    i = -1
    j = len(arr)

    while True:
        while True:
            i += 1
            if arr[i] >= 0:
                break

        while True:
            j -= 1
            if arr[j] <= 0:
                break

        if i >= j:
            break

        _swap(arr, i, j)


if __name__ == '__main__':
    nums = [-12, 18, 10, -15]
    hoare(nums)
    print(nums)
