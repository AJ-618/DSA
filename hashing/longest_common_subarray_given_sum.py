"""
Find the longest common subarray between two
binary arrays with the given sum, regardless
of the index's position. Both the array's will
be of same length.

i/p arr1: [0, 1, 0, 0, 0, 0]
i/p arr2: [1, 0, 1, 0, 0, 1]
o/p: 4, from index 1 to 5

i/p arr1: [0, 0, 0]
i/p arr2: [1, 1, 1]
o/p: 0
"""

def longest_common_subarr_2_arr(arr1: list, arr2: list):
    """Longest common subarr b/n two arr's"""

    def _compute_diff(arr1: list, arr2: list) -> list:
        "compute a diff array from the two arrays"

        n = len(arr1)
        res = [0] * n

        for i in range(n):
            res[i] = arr1[i] - arr2[i]

        return res

    # Return the length of the longest subarr with sum 0
    def _longest_subarr_given_sum(arr: list, k: int) -> int:
        """Find the len of the longest subarr with the
        given sum"""

        m = {}

        n = len(arr)
        pre_sum = 0
        res = 0

        for i in range(n):
            pre_sum += arr[i]

            if pre_sum == k:
                res = i + 1

            if pre_sum not in m:
                m[pre_sum] = i

            if pre_sum - k in m:
                res = max(res, i - m[pre_sum - k])

        return res

    # Compute diff of the two arrays
    diff_arr = _compute_diff(arr1, arr2)

    # return the length of the longest subarray with sum 0
    return _longest_subarr_given_sum(diff_arr, 0)


if __name__ == '__main__':
    nums1 = [0, 1, 0, 0, 0, 0]
    nums2 = [1, 0, 1, 0, 0, 1]
    print(longest_common_subarr_2_arr(nums1, nums2))

    nums1 = [0, 0, 0]
    nums2 = [1, 1, 1]
    print(longest_common_subarr_2_arr(nums1, nums2))
