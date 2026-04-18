"""
Find the longest consecutive subsequence of
elements in an array that appear in any order.
By consecutive we mean n, n + 1, n + 2, and so
on.

i/p: [1, 9, 3, 4, 2, 20]
o/p: 4

i/p: [8, 20, 7, 30]
o/p: 2

i/p: [20, 30, 40]
o/p: 1

Time Complexity -> O(n)

NOTE: We are performing twice the number of lookups of the
length of the array.
"""

def cons_subs(arr: list) -> int:
    """Find longest consecutive subsequence
    in an array."""

    s = set(arr)
    res = 1

    for val in arr:
        if val - 1 not in s:
            curr = 1
            while val + curr in s:
                curr += 1
            res = max(res, curr)

    return res


if __name__ == '__main__':
    nums = [1, 9, 3, 4, 2, 20]
    print(cons_subs(nums))  # 4
