"""
Problem Summary:
----------------
You are given an integer array `prices` where `prices[i]` represents the price of the ith item in a shop.

Special Discount Rule:
- For each item `i`, you can receive a discount equal to `prices[j]` where `j` is the minimum index such that `j > i` and `prices[j] <= prices[i]`.
- If no such `j` exists, no discount is applied.

Goal:
- Return an array `answer` where `answer[i]` is the final price paid for the ith item, considering the special discount.

    Examples:
---------
1. Input: prices = [8, 4, 6, 2, 3]
   Output: [4, 2, 4, 2, 3]
   Explanation:
   - prices[0] = 8 -> Discount = 4 -> Final Price = 8 - 4 = 4
   - prices[1] = 4 -> Discount = 2 -> Final Price = 4 - 2 = 2
   - prices[2] = 6 -> Discount = 2 -> Final Price = 6 - 2 = 4
   - prices[3] = 2 -> No Discount -> Final Price = 2
   - prices[4] = 3 -> No Discount -> Final Price = 3

2. Input: prices = [1, 2, 3, 4, 5]
   Output: [1, 2, 3, 4, 5]
   Explanation: No discounts apply for any item.

3. Input: prices = [10, 1, 1, 6]
   Output: [9, 0, 1, 6]
   Explanation:
   - prices[0] = 10 -> Discount = 1 -> Final Price = 10 - 1 = 9
   - prices[1] = 1 -> Discount = 1 -> Final Price = 1 - 1 = 0
   - prices[2] = 1 -> No Discount -> Final Price = 1
   - prices[3] = 6 -> No Discount -> Final Price = 6

Constraints:
------------
- 1 <= prices.length <= 500
- 1 <= prices[i] <= 1000

Idea:
------------
- Iterate from left to right
- if current element has value bigger than last in queue -> add index to queue
- Else -> get index of element in queue -> update prices
"""
from collections import deque
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = 0
        res = 0
        for i, d in enumerate(arr):
            max_so_far = max(max_so_far, d)
            if max_so_far == i:
                res += 1
        return res


