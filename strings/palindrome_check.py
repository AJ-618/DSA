"""
Find if the string is a palindrome or not.
Return true if yes, else false.

i/p: racecar
o/p: True

i/p: abccba
o/p: True

i/p: laptop
o/p: False

Time Complexity -> O(n)
Space Complexity -> O(1)
"""

def is_palindrome(string: str) -> bool:
    """Find if 's' is a palindrome or not."""

    s = 0
    e = len(string) - 1

    while s <= e:
        if string[s] != string[e]:
            return False

        s += 1
        e -= 1

    return True


if __name__ == '__main__':
    print(is_palindrome("racecar"))# True
    print(is_palindrome("abccba")) # True
    print(is_palindrome("laptop")) # False
