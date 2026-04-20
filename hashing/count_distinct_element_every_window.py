"""
Find and display the count of distinct elements
in every window of an array of length 'n' where
'k' is the size of the window.

i/p: [10, 20, 20, 10, 30, 40, 10], k = 4
o/p: 2 3 4 3

Time Complexity -> O(n)

NOTE: Good problem
"""

from collections import Counter

def dist_in_window(arr: list[int], k: int):
    """Prints the count of distinct elements in
    each sliding window of size 'k'."""

    if not arr or k <= 0 or k > len(arr):
        raise ValueError("Invalid array or window size.")

    freq    = Counter(arr[:k])   # frequency map for the first window
    result  = [len(freq)]        # distinct count for the first window

    for i in range(k, len(arr)):
        # Slide in the new element
        freq[arr[i]] += 1

        # Slide out the oldest element
        outgoing = arr[i - k]
        freq[outgoing] -= 1
        if freq[outgoing] == 0:
            del freq[outgoing]      # remove to keep len(freq) accurate

        result.append(len(freq))

    return result


if __name__ == '__main__':
    nums = [10, 20, 20, 10, 30, 40, 10]
    print(dist_in_window(nums, 4))  # 2 3 4 3
