class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w =0
        num_0 = 0

        l = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                num_0 +=1

            while num_0 > k:
                if nums[l] == 0:
                    num_0 -=1
                l+=1

            max_w = max(max_w, i-l + 1)

        return max_w