# https://leetcode.com/problems/jump-game-ii
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps, last = 0,0
        max_idx = 0
        for i in range(0, n-1):
            if nums[i] + i > max_idx:
                max_idx = nums[i] + i
            if i == last:
                jumps+=1
                last = max_idx
        return jumps
