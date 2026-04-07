"""
Find an subarray in the array with the given sum.

i/p: [8, 34, 12, -4, 21, 5, -10, 6], k = 24
o/p: True
"""

def find_sum(arr: list, k: list) -> bool:
    """Find subarray with given sum 'k'."""

    s = set()
    pre_sum = 0

    for val in arr:
        pre_sum += val

        if pre_sum == k or pre_sum - k in s:
            return True

        s.add(pre_sum)

    return False


if __name__ == '__main__':
    nums = [8, 34, 12, -4, 21, 5, -10, 6]
    print(find_sum(nums, 50))
    print(find_sum(nums, 24))
    print(find_sum(nums, 51))
