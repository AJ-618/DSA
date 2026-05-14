from typing import List

# Rabin-Karp String Matching
# Average Time Complexity:
#   O(n + m)
#
# Worst Case:
#   O(n * m) due to hash collisions
#
# Space Complexity:
#   O(1)
#
# Uses:
#   - Rolling hash
#   - Modular arithmetic
#   - Collision verification


def rabin_karp(text: str, pattern: str) -> List[int]:
    """
    Returns all starting indices where `pattern`
    occurs in `text`.
    """

    n = len(text)
    m = len(pattern)

    if m == 0:
        return list(range(n + 1))

    if m > n:
        return []

    # Base for characters
    BASE = 256

    # Large prime modulus
    MOD = 1_000_000_007

    # BASE^(m-1) % MOD
    high_base = pow(BASE, m - 1, MOD)

    pattern_hash = 0
    window_hash = 0

    # Initial hash computation
    for i in range(m):
        pattern_hash = (pattern_hash * BASE + ord(pattern[i])) % MOD
        window_hash = (window_hash * BASE + ord(text[i])) % MOD

    matches = []

    for i in range(n - m + 1):

        # Hash match -> verify to avoid collision issues
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                matches.append(i)

        # Roll the hash window
        if i < n - m:
            outgoing = ord(text[i])
            incoming = ord(text[i + m])

            window_hash = (
                (window_hash - outgoing * high_base) * BASE
                + incoming
            ) % MOD

            # Ensure positive hash
            if window_hash < 0:
                window_hash += MOD

    return matches


if __name__ == "__main__":
    text = "ababcabcabababd"
    pattern = "abab"

    result = rabin_karp(text, pattern)

    print("Matches found at indices:", result)
