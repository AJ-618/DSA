"""
Find the length of the longest subarray in the
array with the given sum else return False.

i/p: [2, -1, 8, 7, -4, 9, -3, 8], k = 9
o/p: 4

Time complexity: Theta(n)

NOTE: Good Problem
"""

def longest_subarr(arr: list, k: int) -> int:
    """Find the len of the longest subarr with the
    given sum"""

    m = {}

    n = len(arr)
    pre_sum = 0
    res = 0

    for i in range(n):
        pre_sum += arr[i]

        if pre_sum == k:
            res = i + 1

        if pre_sum not in m:
            m[pre_sum] = i

        if pre_sum - k in m:
            res = max(res, i - m[pre_sum - k])

    return res


if __name__ == '__main__':
    nums = [2, -1, 8, 7, -4, 9, -3, 8]
    print(longest_subarr(nums, 16))  # 6
