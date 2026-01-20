"""
------------ Minimum Difference in an Array ------------

i/p: [1, 8, 12, 5, 18]
o/p: 3

i/p: [8, 15]
o/p: 7

i/p: [8, -1, 0, 3]
o/p: 1

i/p: [10]
o/p: INF

Time complexity -> O(nlogn) Average case
"""

def min_diff(arr: list) -> int:
    "Find min diff in array"

    n = len(arr)
    diff = float('inf')

    # Using Timsort, highly optimized sorting algo for python
    arr.sort()

    for i in range(1, n):
        diff = min(diff, abs(arr[i] - arr[i - 1]))

    return diff


if __name__ == '__main__':
    print(min_diff([1, 8, 12, 5, 18]))  # 3
    print(min_diff([8, 15]))            # 7
    print(min_diff([8, -1, 0, 3]))      # 1
    print(min_diff([10]))               # inf
