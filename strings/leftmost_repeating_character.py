"""
Find the index of the leftmost repeating
character in the string.

i/p: "abbccb"
o/p: 1 -> 1 is index of b

i/p: "geeksforgeeks"
o/p: 0 -> 0 is index of g

i/p: "abcd"
o/p: -1 -> -1 as no repeating string found
"""

def leftmost_repeating_string(s: str) -> int:
    """Find the index of the leftmost repeating
    character in the string."""

    seen = {}
    leftmost = float('inf')
    
    for i, char in enumerate(s):
        if char in seen:
            leftmost = min(leftmost, seen[char])
        else:
            seen[char] = i
            
    return leftmost if leftmost != float('inf') else -1


if __name__ == '__main__':
    print(leftmost_repeating_string("abbccb"))           # 1
    print(leftmost_repeating_string("geeksforgeeks"))   # 0
    print(leftmost_repeating_string("abcd"))            # -1
