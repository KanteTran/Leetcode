# https://leetcode.com/problems/h-index
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        for i in range(n):
            if citations[i] < i+1:
                return i
        return n