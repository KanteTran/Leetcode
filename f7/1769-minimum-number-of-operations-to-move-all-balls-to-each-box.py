# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)

        ball_from_left = ball_from_right = 0
        total_operation_left = total_operation_right = 0

        for d in range(len(boxes)):
            res[d] += total_operation_left
            ball_from_left += int(boxes[d])
            total_operation_left += ball_from_left

            res[len(boxes) - d - 1] += total_operation_right
            ball_from_right += int(boxes[(len(boxes) - d - 1)])
            total_operation_right += ball_from_right

        return res