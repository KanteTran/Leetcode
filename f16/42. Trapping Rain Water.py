class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = height[0], height[-1]

        res = 0

        start, end = 0, len(height) - 1

        while start < end:
            if max_left < max_right:
                start += 1
                max_left = max(height[start], max_left)
                res += max_left - height[start]
            else:
                end -= 1
                max_right = max(height[end], max_right)
                res += max_right - height[end]

        return res
