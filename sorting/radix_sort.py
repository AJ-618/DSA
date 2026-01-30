"""
--------- Radix Sort ---------

- Like counting sort, it is a linear time algorithm
  if our data is within a limited range. But unlike
  counting sort, it works in linear time even if
  the data or 'k' is within the range of n^2 or n^3.
- It uses counting sort as a subroutine to sort the
  elements.
- Like counting sort, it is not a comparison based
  algorithm.
- In Radix sort, the first step is to find out the
  number of digits in the largest number. Then we
  prefix zeroes to the numbers that don't have the
  same digits has the max number. Then we sort the
  prefixed numbers in increasing order according to
  the last digit, then middle and then first. Suppose
  the max number in the array had 4 digits, then we
  would require 4 passes.
- Time Complexity - Theta(d*(n+b)), where 'd' is the
  max number of digits, 'n' the length of the array,
  and 'b' the base we are taking, i.e. 10 for decimal
  system.
- Space Complexity - Theta(n + b) extra space where
  'n' is the length of the array and 'b' the base of
  the number system used.
- An interesting fact about Radix sort is that if 'b'
  increases, then 'd' decreases, but the extra space
  required increases.
"""

def _counting_sort(arr: list, n: int, exp: int):
    count = [0] * 10 # 0-9 eq 10
    output = [0] * n

    # Create count array
    for val in arr:
        index = (val // exp) % 10
        count[index] += 1

    # Create cumulative count array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Reverse-traverse and do stable sorting
    for i in range(n - 1, -1, -1):
        val = arr[i]
        x = (val // exp) % 10
        index = count[x] - 1
        output[index] = val
        count[x] -= 1

    # Copy sorted elems in-place
    arr[:] = output

def radix_sort(arr: list):
    "radix sort"

    n = len(arr)
    max_elem = max(arr)

    exp = 1
    while (max_elem // exp) > 0:
        print('arr', arr)
        _counting_sort(arr, n, exp)
        exp *= 10


if __name__ == '__main__':
    nums = [319, 212, 6, 8, 100, 50]
    radix_sort(nums)
    print(nums)
