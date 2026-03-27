"""
Print intersection of two unsorted arrays

i/p: [8, 12, 46, 20], [10, 5, 21, 8, 50, 46]
o/p: 8 46

Simply use a python set (unique values) from
array2 and traverse array1 and check if any
value intersects.

Time Complexity -> O(m + n)
"""

def intersection(arr1: list, arr2: list):
    "Find intersection of two arr's"

    s = set(arr2)
    for val in arr1:
        if val in s:
            print(val, sep=' ', end=' ')


if __name__ == '__main__':
    nums1 = [8, 12, 46, 20]
    nums2 = [10, 5, 21, 8, 50, 46]

    intersection(nums1, nums2)
