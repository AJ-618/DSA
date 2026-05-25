"""
Search for an anagram in a string.

i/p: string = "geeksforgeeks", anagram = "frog"
o/p: True
"""

from collections import Counter

def find_anagrams(text: str, pattern: str) -> list[int]:
    """
    Finds all starting indices of pattern's anagrams in text.
    Time Complexity: O(len(text))
    Space Complexity: O(1) - since the alphabet size is fixed (max 26 or 256 keys)
    """
    result = []
    p_len, t_len = len(pattern), len(text)
    
    if p_len > t_len or p_len == 0:
        return result
    
    # Frequency maps for pattern and the current window in text
    p_count = Counter(pattern)
    window_count = Counter()
    
    # Initialize the first window
    for i in range(p_len):
        window_count[text[i]] += 1
        
    # Check if the first window is a match
    if window_count == p_count:
        result.append(0)
        
    # Slide the window across the text
    for i in range(p_len, t_len):
        # Add the new character entering the window
        start_char_to_add = text[i]
        window_count[start_char_to_add] += 1
        
        # Remove the old character leaving the window
        char_to_remove = text[i - p_len]
        if window_count[char_to_remove] == 1:
            del window_count[char_to_remove]  # Clean up key to keep dict comparison fast
        else:
            window_count[char_to_remove] -= 1
            
        # If the window matches the pattern count, we found an anagram
        if window_count == p_count:
            result.append(i - p_len + 1)
            
    return result


if __name__ == '__main__':
    text_str = "cbaebabacd"
    pattern_str = "abc"
    print(f"Anagrams of '{pattern_str}' found at indices:", find_anagrams(text_str, pattern_str))
