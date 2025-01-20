# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = []
        c = 0
        for x in arr:
            if x %k == 0:
                c+=1
            else:
                d.append(x%k)
        if c %2 != 0:
            return False 
        d = sorted(d)
        n = len(d)
        for i in range(n):
            if (d[i] + d[n-1-i]) % k != 0:
                return False
        return True
