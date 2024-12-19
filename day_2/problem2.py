# https://leetcode.com/problems/max-chunks-to-make-sorted/
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        chunks = 0
        correct_sum = 0
        crr_sum = 0
        for i in range(0, n):
            correct_sum+=i
            crr_sum+=arr[i]

            if correct_sum == crr_sum:
                chunks+=1
        return chunks