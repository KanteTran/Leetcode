# https://leetcode.com/problems/max-consecutive-ones-iii/
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        for i in range(len(nums)):
            if nums[i] == 0:
                k-=1
            if k < 0:
                if nums[l] == 0:
                    k+=1
                l+=1
        return i-l+1
                