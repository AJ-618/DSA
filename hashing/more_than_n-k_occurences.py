"""
Find the elements in an array with more
than n/k occurences, where 'n' is the
length of the array and 'k' is the given
integer.

i/p: [30, 10, 20, 20, 10, 20, 30, 30], k = 4
o/p: 20 30
In this case, n/k equals 2 as length of the
array is 8 and k is 4.

Time Complexity -> O(n + m), where n is the length of
the array and m the length of the freq array.

Space Complexity -> O(m + k), where m is the space required
to create the frequency array and k the space required to
create the returning array result.

NOTE: In case, k is a very small integer when compared to n,
then use a frequency map may not be a good idea. A better way
in that case would be to use Moore's voting algorithm.

CRITERIA (for above note): k * (n/k + 1) <= n 
"""

from collections import Counter

def occurences(arr: list[int], k: int) -> list[int]:
    """Find elements with more than n/k occurences."""

    x = len(arr) / k
    res = []

    freq_map = Counter(arr)

    for val, freq in freq_map.items():
        if freq > x:
            res.append(val)

    return res


if __name__ == '__main__':
    nums = [30, 10, 20, 20, 10, 20, 30, 30]
    print(occurences(nums, 4))  # 20 30
