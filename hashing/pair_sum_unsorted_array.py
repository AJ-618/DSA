"""
Find a pair in the array that is equal to
the given sum.

i/p: [8, 3, 4, 2, 5], sum = 6
o/p: True
"""

def pair(arr: list, _sum: int) -> bool:
    """Find pair that is equal to the
    given sum."""

    s = set()
    for val in arr:
        if _sum - val not in s:
            s.add(val)
            continue
        return True

    return False


if __name__ == '__main__':
    nums = [8, 3, 4, 2, 5]
    print(pair(nums, 6))    # True
