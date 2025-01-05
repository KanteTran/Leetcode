class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        for i, d in enumerate(citations):
            if d >= len(citations) - i:
                return len(citations) - i
        return 0