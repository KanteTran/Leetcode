# https://leetcode.com/problems/minimum-size-subarray-sum
from types import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        min_arr = len(nums) + 1
        start = 0
        for i in range(0, len(nums)):
            s+= nums[i]
            while (s >= target):
                min_arr = min(i - start + 1, min_arr)
                s-=nums[start]
                start +=1
        
        return min_arr if min_arr <= len(nums) else 0

        