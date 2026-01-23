"""
-------- Sort an Array with three types of Elements --------

i/p: [0, 1, 1, 2, 0, 1]
o/p: [0, 0, 1, 1, 1, 2]

Problem: We have to sort an array with 3 types of elements.

Approach: Use Dutch National Flag Algorithm (Hoare partition variation)

Time -> Theta(n) 1 traversal, Space -> Theta(1)
"""

def sortx(arr: list):
    """Dutch National Algorithm"""
    def _swap(arr: list, x: int, y: int):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp

    l = 0
    m = 0
    h = len(arr) - 1

    while m <= h:
        if arr[m] == 0:
            _swap(arr, l, m)
            l += 1
            m += 1
        elif arr[m] == 1:
            m += 1
        else:
            _swap(arr, m, h)
            h -= 1


if __name__ == '__main__':
    nums = [0, 1, 1, 2, 0, 1]
    sortx(nums)
    print(nums)
