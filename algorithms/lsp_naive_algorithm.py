"""
Naive implementation to calculate longest prefix suffix array
from a string.

Time Complexity -> O(n^3)
"""

def lfs_arr(s: str) -> list[int]:
    """Naive implementation for KMP algorithm"""

    def _long_pre_suff(s: str, n: int):
        
        for len in range(n - 1, 0, -1):
            flag = True

            for i in range(len):
                if s[i] != s[n - len + i]:
                    flag = False

            if flag == True:
                return len

        return 0


    n = len(s)
    lps = []

    for i in range(n):
        lps.append(_long_pre_suff(s, i + 1))

    return lps


if __name__ == '__main__':
    string = "ababacab"
    print(lfs_arr(string))
