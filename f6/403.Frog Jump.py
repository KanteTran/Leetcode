from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {i: set() for i in stones}
        # first is the jump
        # second is the can jump into

        dp[stones[0]].add(0)
        for loc in stones:
            possible_jumps = dp[loc]
            next_steps = [jump + step for jump in possible_jumps for step in [-1, 0, 1] if jump + step > 0]

            for step in next_steps:
                if loc + step in dp:
                    dp[loc + step].add(step)
        # print(dp)
        return len(dp[stones[-1]]) != 0

if __name__ == '__main__':
    Solution().canCross([0,1,3,5,6,8,12,17])