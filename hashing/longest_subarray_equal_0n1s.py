"""
Find the length of the longest subarray with
equal numbers of zeroes and ones in a binary
array.

NOTE: the elements have to be contagious; also
a good problem with an intersting solution.

Tip: Replace 0s with -1's and find the longest
subarray with the sum 0.

i/p: [1, 0, 1, 1, 1, 0, 0]
o/p: 6

i/p: [1, 1, 1, 1]
o/p: 0

Time complexity -> Theta(n) or more specifically
Theta(n^2)
"""

def max_len(arr: list) -> int:
    """Find len longest subarray with
    equal number of zeroes and ones."""

    def _longest_subarr(arr: list, k: int) -> int:
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

    # Replacing 0's with -1
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1

    # Find the longest subarray with 0 sum
    return _longest_subarr(arr, 0)


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 1, 0, 0]
    print(max_len(nums)) # 6
