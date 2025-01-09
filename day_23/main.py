# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        n = len(digits)
        for i in range(n-1, -1, -1):
            if c == 0:
                break
            tmp = digits[i] + c
            c = tmp // 10 if tmp > 9 else 0
            digits[i] = tmp % 10
        return  [c] + digits if c > 0 else digits
