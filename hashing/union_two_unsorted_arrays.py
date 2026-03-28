"""
Create union of two unsorted arrays.

Pythonic Solution -> create a set from the
two unsorted arrays and find its length.

Time complexity -> O(m + n)
"""

def union(arr1: list, arr2: list) -> tuple[set, int]:
    """Create union from two unsorted arrays
    and return the final set and its length."""

    s = {*arr1, *arr2}
    return (s, len(s))


if __name__ == '__main__':
    nums1 = [15, 20, 5, 15]
    nums2 = [15, 15, 15, 20, 10]

    print(union(nums1, nums2))
