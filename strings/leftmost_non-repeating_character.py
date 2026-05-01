"""
Find the leftmost non-repeating character in
the string.

i/p: "geeksforgeeks"
o/p: 5

i/p: "apple"
o/p: 0

i/p: "abcda"
o/p: 1

Time complexity -> Theta(n)
Space complexity -> O(n) where 'n' is the number
                    of unique characters in the string.
"""

def non_rep(s: str) -> int:
    """Find leftmost non-repeating character."""

    seen = []
    leftmost = float('inf')

    for i in range(len(s) - 1, -1, -1):
        if s[i] not in seen:
            seen.append(s[i])
            leftmost = min(leftmost, i)

    return leftmost


if __name__ == '__main__':
    print(non_rep("geeksforgeeks")) # 5
    print(non_rep("apple"))         # 0
    print(non_rep("abcda"))         # 1
