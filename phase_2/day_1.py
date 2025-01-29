
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                j = mid - 1
            elif target > nums[mid]:
                i = mid + 1
        return mid + 1 if nums[mid] < target else mid
        
        