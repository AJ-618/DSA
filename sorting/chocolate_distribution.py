"""
--------- Chocolate Distribution Problem ---------

i/p: [7, 3, 1, 8, 9, 12, 56], m = 3
o/p: = 6 -> [1, 3, 7]

Problem: The array contains packets with number of chocolates
in them. We need to find 'm' number of packets with the least
variation or difference between them such that every body gets
almost the same number of chocolates.

Approach: sort, then return arr[m - 1] - arr[0]. Use tim sort.

Time -> O(nlogn)
"""

def choc_dist(arr: list, m: int) -> int:
    "Chocolate distribution implementation"

    if m > len(arr):
        return -1

    arr.sort()
    return arr[m - 1] - arr[0]


if __name__ == '__main__':
    print(choc_dist([7, 3, 1, 8, 9, 12, 56], 3)) # 6
