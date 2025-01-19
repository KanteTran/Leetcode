class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        start, end = 0, len(nums)-1

        while start <= end:
            s = nums[start]

            while start< end and nums[start] + 1 == nums[start+1] :
                start +=1

            if nums[start] !=s:
                res.append(f"{s}->{nums[start]}")
            else:
                res.append(f"{s}")

            start +=1

        return res