"""
KMP algorithm used to match a pattern in a string.

i/p: text = "abcdefgh", pattern = "bcd"
o/p: 1

i/p: text = "aaaaab", pattern = "aaaa"
o/p: 0 1

i/p: text = "abcd", pattern = "ba"
o/p: None

Time Complexity -> O(n + m) where 'n' is the length of the text and
                   'm' is the length of the pattern

Space Complexity -> O(n) to return the indices of the patterns matched
"""

def fill_lps(s: str) -> list[int]:
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


def kmp_pattern(text: str, pattern: str) -> list[int]:
    """KMP implementation for pattern matching in a
    string."""
    
    n = len(text)
    m = len(pattern)

    lps = fill_lps(pattern)

    res = []

    i = 0
    j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            res.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

    return res


if __name__ == '__main__':
    text1 = "abcdefgh"
    pattern1 = "bcd"
    print(kmp_pattern(text1, pattern1))

    text2 = "aaaaab"
    pattern2 = "aaaa"
    print(kmp_pattern(text2, pattern2))

    text3 = "abcd"
    pattern3 = "ba"
    print(kmp_pattern(text3, pattern3))
