class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        dp = [{} for _ in range(1000)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                res = max(res, dp[i][diff])

        return res