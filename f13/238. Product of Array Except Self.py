class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1 for _ in nums]
        left = 1
        right = 1
        for i in range(0, len(nums)):
            res[i] = left
            left *= nums[i]

        for i in range(length-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res
