"""
Find if two strings are anagrams of each other.

i/p: silent, listen
o/p: True

i/p: car, cat
o/p: False

Time Complexity -> O(n)
Space Complexity -> O(k) where k = unique chars
"""

from collections import Counter

def is_anagram(s1: str, s2: str) -> bool:
    """Find if s1 and s2 are anagrams."""

    if len(s1) != len(s2):
        return False
    
    return Counter(s1) == Counter(s2)


if __name__ == '__main__':
    print(is_anagram("silent", "listen"))   # True
    print(is_anagram("car", "cat"))         # False
    print(is_anagram("qwerty", "qwer"))     # False
