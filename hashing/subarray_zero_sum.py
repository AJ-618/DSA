"""
Find an subarray within the array and return
True if there exists an array with the sum
zero, else return False.

Idea: calculate pre-sum and add it in the set.
If the pre-sum is zero or is in the set, it means
that we have elements at indexes that have zero sum.

i/p: [1, 4, 13, -3, -10, 5]
o/p: yes

Time Complexity -> O(n)
"""

def zero_sum(arr: list) -> bool:
    """Find subarray with zero sum"""

    s = set()
    pre_sum = 0
    n = len(arr)

    for i in range(n):
        pre_sum += arr[i]

        if pre_sum in s or pre_sum == 0:
            return True

        s.add(pre_sum)

    return False


if __name__ == '__main__':
    nums = [1, 4, 13, -3, -10, 5]
    print(zero_sum(nums))
