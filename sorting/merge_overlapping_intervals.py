"""
--------- Merge Overlapping Intervals ---------

i/p: [[5, 10], [3, 15], [18, 30], [2, 7]]
o/p: [[2, 15], [18, 30]]

Problem: merge overlapping intervals
"""

def merge(arr: list):
    "Merge overlapping intervals"
    # Timsort, O(nlogn) in-place
    arr.sort(key=lambda x: x[0]) # Custom quicksort algo can be
                                 # implemented here
    res = 0
    for i in range(1, len(arr)):
        if arr[res][1] >= arr[i][0]:
            arr[res][1] = max(arr[res][1], arr[i][1])
            arr[res][0] = min(arr[res][0], arr[i][0])
        else:
            res += 1
            arr[res] = arr[i]

    del arr[res+1:]


if __name__ == '__main__':
    nums = [[5, 10], [3, 15], [18, 30], [2, 7]]
    merge(nums)
    print(nums)
