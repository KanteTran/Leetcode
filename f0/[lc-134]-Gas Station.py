from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1

        sum_ = 0
        start = 0

        for i in range(len(gas)):
            sum_ += gas[i] - cost[i]
            if sum_ < 0:
                sum_ = 0
                start = i + 1

        return start