class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        n = len(s)
        if n == k: return True
        if n < k: return False

        freq = {}
        for c in s:
            if freq.get(c):
                freq[c]+=1
            else:
                freq[c] = 1
        rs = 0
        for c,v in freq.items():
            if v % 2 == 1:
                rs = rs + 1
        if rs > k :
            return False
        return True
