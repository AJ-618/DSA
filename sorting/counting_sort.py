"""
--------- Counting Sort ---------

- Counting sort is a linear time algorithm for cases
  when our input elements are in a small range.
- For example, if we have 'n' elements, and the elements
  are in the range of zero to 'k-1', then counting
  sort will take Theta(n + k) time.
- It is not a comparison based algorithm, it never compares
  items with each other. Counting sort is useful only when
  'k' is linear in terms of 'n'. When 'k' becomes 'nlogn',
  or quadratic, its of no use because we have better 
  comparison based algorithms for that.
- It is a stable sorting algorithm.
- We can sort objects with a particular key as well.
- It requires Theta(n + k) space.
- It is used as a subroutine in Radix sort.
- NOTE: This algorithm is only useful when 'k' is small.
  If it is large, it becomes a n^2 or n^3 algorithm. And
  this is where Radix sort is a better algorithm. It works
  in linear time regardless of the range of 'k'.
"""

def count_sort(arr: list, k: int):
    "Count Sort"

    n = len(arr)
    count = [0] * k
    output = [0] * n

    for val in arr:
        count[val] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        val = arr[i]
        index = count[val]
        output[index - 1] = val
        count[val] -= 1

    arr[:] = output


if __name__ == '__main__':
    nums = [1, 4, 4, 1, 0, 1, 2, 2, 1]
    count_sort(nums, 5)
    print(nums)
