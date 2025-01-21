class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l, loc = 0, 0, {}

        for i, d in enumerate(s):
            if d in loc and loc[d] >= l:
                l = loc[d] + 1

            loc[d] = i

            res = max(res, i - l + 1)

        return res
