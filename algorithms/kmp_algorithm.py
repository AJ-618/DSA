"""
KMP algorithm used to calculate longest prefix suffix array
of a string in linear time.

Time Complexity -> O(n)
"""

def kmp(s: str) -> list[int]:
    n = len(s)
    lps = [0] * n

    l = 0
    i = 1

    while i < n:
        if s[i] == s[l]:
            l += 1
            lps[i] = l
            i += 1

        else:
            if l != 0:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


if __name__ == '__main__':
    string = "ababacab"
    print(kmp(string))
