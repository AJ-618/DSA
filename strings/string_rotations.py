"""
Check if given string is rotation of the other
string.

i/p: s1 = "ABAB", s2 = "ABBA"
o/p: False

i/p: "ABCD", s2 = "CDAB"
o/p: True
"""

def is_rotation(s1: str, s2: str) -> bool:
    # If lengths don't match, they can't be rotations
    if len(s1) != len(s2) or not s1:
        return False
    
    # Check if s2 is a substring of s1 concatenated with itself
    return s2 in (s1 + s1)


if __name__ == '__main__':
    print(is_rotation("ABAB", "ABBA"))
    print(is_rotation("ABCD", "CDAB"))
