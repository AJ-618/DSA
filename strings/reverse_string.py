"""
Reverse the words in a string

i/p: "I love coding"
o/p: "coding love I"

i/p: "abc"
o/p: "abc"

Time complexity -> O(n)
Space complexity -> O(n) where n is the length of the string

NOTE: O(1) space implementations are available in languages like
c++ and java as their strings are immutable which is not the case
in python.
"""

def reverse_string(s: str) -> str:
    """Reverses the words in a string"""

    wl = s.split()  # O(n) time
    n = len(wl)

    if n <= 1:
        return s

    x = 0
    y = n - 1

    while x < y:    # O(n) time
        wl[x], wl[y] = wl[y], wl[x]

        x += 1
        y -= 1

    return ' '.join(wl) # O(n) time


if __name__ == '__main__':
    print(reverse_string("I love coding"))
    print(reverse_string("abc"))
