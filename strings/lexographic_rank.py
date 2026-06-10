"""
Find the lexographic rank of a string.

i/p: "ABC"
o/p: 6

i/p: "BAC"
o/p: 3
"""

from collections import Counter
from math import factorial

def get_lexicographic_rank(s: str) -> int:
    """
    Finds the 1-based lexicographical rank of a string.
    Handles strings with both unique and duplicate characters.
    """
    n = len(s)
    # Total count of each character in the string
    char_counts = Counter(s)
    
    # Sort the unique characters to easily find how many are smaller
    sorted_chars = sorted(char_counts.keys())
    
    rank = 1  # Start at rank 1
    
    # Calculate initial denominator for duplicate permutations: (n1! * n2! * ...)
    freq_factorial_prod = 1
    for count in char_counts.values():
        freq_factorial_prod *= factorial(count)
        
    # Total permutations of the string length = n! / (n1! * n2! * ...)
    # We will dynamically update this value as we move left-to-right
    current_permutations = factorial(n) // freq_factorial_prod

    # Process the string from left to right
    for i in range(n):
        # Remaining characters to be placed after index i
        remaining_len = n - i
        
        # Total permutations for the remaining slot length
        current_permutations = (current_permutations * char_counts[s[i]]) // remaining_len
        
        # Count how many available characters are strictly smaller than s[i]
        for char in sorted_chars:
            if char >= s[i]:
                break  # Since sorted_chars is sorted, we can stop here
                
            if char_counts[char] > 0:
                # If we placed 'char' at the current position instead of s[i],
                # how many valid permutations would that create?
                # Formula: (current_permutations * count_of_char) / count_of_s[i]
                rank += (current_permutations * char_counts[char]) // char_counts[s[i]]
        
        # Reduce the count of the current character as it is now fixed
        char_counts[s[i]] -= 1

    return rank


# --- Example Usage ---
if __name__ == "__main__":
    # Example 1: Standard string with unique characters
    str1 = "CBA"
    print(f"Rank of '{str1}': {get_lexicographic_rank(str1)}")  # Output: 6

    # Example 2: String with duplicate characters
    str2 = "BOOK"
    print(f"Rank of '{str2}': {get_lexicographic_rank(str2)}")  # Output: 3
    
    # Example 3: Academic standard test case
    str3 = "STRING"
    print(f"Rank of '{str3}': {get_lexicographic_rank(str3)}")  # Output: 598
