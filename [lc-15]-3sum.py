class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, n-1
            while left < right :
                total = nums[i] + nums[left] + nums[right]
                if total == 0 :
                    res.append([nums[i], nums[left], nums[right]])
                    while nums[left] == nums[left+1] and left +1 < right:
                        left+=1
                    while nums[right] == nums[right-1] and right -1> left:
                        right -=1
                    left +=1
                    right -=1
                elif total >0 :
                    right -=1
                else:
                    left +=1

        return res