# https://leetcode.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1

        for i in range(0,n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start
            