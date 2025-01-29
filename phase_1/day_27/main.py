# https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean str
        s = re.sub('[^0-9a-zA-Z]+', '', s)
        s = s.lower()
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return False
        return True