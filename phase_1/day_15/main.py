# https://leetcode.com/problems/string-without-aaa-or-bbb
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        n = a+b
        s = []
        freq_a, freq_b = 0, 0
        for i in range(n):
            if (a > b and freq_a < 2) or freq_b == 2:
                s.append('a')
                freq_a, freq_b = freq_a+1, 0
                a-=1
            else:
                s.append('b')
                freq_a, freq_b = 0, freq_b+1
                b-=1        
        return ''.join(s)