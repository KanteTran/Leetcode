# https://leetcode.com/problems/reverse-words-in-a-string
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split(' ')
        out = ''
        for i in range(len(arr)-1, -1, -1):
            if len(arr[i]) == 0:
                continue
            out = out + arr[i] + ' '

        return out.strip()