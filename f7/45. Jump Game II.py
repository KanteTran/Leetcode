class Solution:
    def jump(self, nums: List[int]) -> int:
        res  = [1e9 for _ in nums]
        res[0] = 0

        for i in range(0, len(nums)):
            for j in range(0, nums[i]+1):
                if  i+j < len(nums):
                    res[i+j] = min(res[i + j], res[i] + 1)

        return res[len(nums)-1]