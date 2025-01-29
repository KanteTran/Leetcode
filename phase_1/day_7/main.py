# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""
Remove duplicates in-place such that duplicates appeared at most twice and return the new length.
Solution: Two pointers i, w_idx. Rewrite array with: valid value if current value diff with two previous value else skip.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w_idx = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[w_idx - 2]:
                nums[w_idx] = nums[i]
                w_idx += 1

        return w_idx