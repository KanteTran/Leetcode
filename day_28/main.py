# https://leetcode.com/problems/product-of-array-except-self/submissions/1508166364/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        suff = 1
        for i in range(1, n):
            out[i] = nums[i-1] * out[i-1]
        # print(out)
        for i in range(n-1, -1, -1):
            out[i] = out[i] * suff 
            suff*=nums[i]
        
        return out