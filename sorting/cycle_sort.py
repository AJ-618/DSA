"""
--------- Cycle Sort ---------

1. O(n^2) worst case
2. Does minimum memory writes and can be useful
   for cases where memory writes are costly.
3. In-place and not stable
4. Useful to solve queries like find minimum swaps
   required to sort an array.

Approach: for each element we calculate number of elements
smaller than it.
"""

def cycle(arr: list):
    "Cycle sort"

    n = len(arr)

    for i in range(0, n - 2):
        curr_elem = arr[i]
        pos = i

        for j in range(i + 1, n):
            if arr[j] < curr_elem:
                pos += 1

        arr[pos], curr_elem = curr_elem, arr[pos]
        print('arr', arr)
        while i != pos:
            pos = i
            for j in range(i + 1, n):
                if arr[j] < curr_elem:
                    pos += 1
            arr[pos], curr_elem = curr_elem, arr[pos]


if __name__ == '__main__':
    nums = [20, 40, 10, 50, 30]
    cycle(nums)
    print(nums)
