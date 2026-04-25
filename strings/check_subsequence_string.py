"""
Check if a given string is a subsequent string of
the provided string.

i/p: "ABCD", "AD"
o/p: True

i/p: "ABCDE", "AED"
o/p: False

Time Complexity -> O(m + n) where 'm' is the length
of original string and 'n' is the length of the provided
substring.

Space Complexity -> O(1)

NOTE: There also exists a recursive solution.
"""

def is_subs(string: str, subs: str) -> bool:
    """Find if 'str' is a subsequent string
    of 'string' or not."""

    i           = 0
    j           = 0
    subs_len    = len(subs)
    string_len  = len(string)

    while i < string_len and j < subs_len:
        if string[i] == subs[j]:
            j += 1

        i += 1

    return j == subs_len


if __name__ == '__main__':
    print(is_subs("ABCD", "AD"))      # True
    print(is_subs("ABCDE", "AED"))    # False
