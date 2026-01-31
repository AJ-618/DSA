"""
--------- Bucket Sort ---------

- Bucket sort is a sorting algorithm that works in
  linear time when our data is uniformly distributed
  across a range.
- In bucket sort, we divide the range into five buckets.
  We could also have didvided the range into ten buckets
  but in the end it all about time vs space tradeoff.
  Then we traverse the array and put the elements in their
  respective buckets. After the elements have been put into
  their respective buckets, we sort the individual buckets.
  We can use any standard sorting algorithm to sort the 
  buckets. If we are sure that the individual buckets are 
  going to have less number of elements, then we can use 
  insertion sort as it is the best suitable algorithm for 
  small amount of data.
- The question arises that how many elements are going to
  be there in the individual buckets. If we have 'n' elements
  and 'k' buckets, then we are going to have 'n/k' elements
  in each bucket.
- Please note that this algorithm might work really bad if
  your data is not uniformly distributed.
- Best case time complexity assuming 'k ~ n' -> O(n)
- Worst case time complexity -> O(n^2) if we are using insertion
  sort to sort the individual buckets. But if we are using
  nlogn algorithms, then the time complexity would be O(nlogn).
- NOTE: Bucket sort is the best algorithm if our data is uniformly
  distributed across the range.
"""

from itertools import chain

def bucket_sort(arr: list, k: int):
    "bucket sort implementation"

    n = len(arr)
    if n < 2:
        return

    max_elem = max(arr)
    x = (max_elem // k) + 1   # 1st bucket range

    # Creating 'k' buckets
    buckets = [[] for _ in range(k)]

    # Placing elems in arr to their respective buckets
    for val in arr:
        bi = int(val / x)
        buckets[bi].append(val)

    # Sorting individual buckets
    for bucket in buckets:
        bucket.sort()

    # fastest way to flatten nested list (one level)
    arr[:] = list(chain.from_iterable(buckets))


if __name__ == '__main__':
    nums = [30, 40, 10, 80, 5, 12, 70]
    bucket_sort(nums, 4)
    print(nums)
