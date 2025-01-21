class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        cur = nums[0]

        for i in range(len(nums) - 1):

            if nums[i] < nums[i + 1]:
                cur += nums[i + 1]
            else:
                result = max(cur, result)
                cur = nums[i + 1]

        return max(cur, result)