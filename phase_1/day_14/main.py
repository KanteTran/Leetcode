# https://leetcode.com/problems/rotate-array
"""_summary_
    1: using extra array to store the rotated array
    2: using reverse array (reverse 3 times: 0 to n-1, 0 to k-1, k to n-1)
Returns:
    _type_: _description_
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == k or k == 0:
            return
        k = k%n
        tmp_arr = [0] * n
        for i in range(n):
            tmp_arr[(i+k) % n] = nums[i]
        for i in range(n):
            nums[i] = tmp_arr[i]
