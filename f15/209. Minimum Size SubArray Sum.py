class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 1e9
        curr_sum = 0
        start = 0

        for i, d in enumerate(nums):
            curr_sum += d

            while curr_sum >= target:
                res = min(res, i - start + 1)
                curr_sum -= nums[start]
                start += 1

        return res if res != 1e9 else 0

