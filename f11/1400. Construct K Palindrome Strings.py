class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        if len(s) == k:
            return True

        odd_cnt = 0

        for c in s:
            odd_cnt ^= 1 << (ord(c) - ord("a"))

        return bin(odd_cnt).count("1") <= k
