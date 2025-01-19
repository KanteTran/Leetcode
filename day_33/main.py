
# https://leetcode.com/problems/reach-end-of-array-with-max-score
class Solution(object):
    def findMaximumScore(self, nums):
        max_val = 0
        total_sum = 0
        for i in range(len(nums) - 1):
            max_val = max(max_val, nums[i])
            total_sum += max_val
        return total_sum
        