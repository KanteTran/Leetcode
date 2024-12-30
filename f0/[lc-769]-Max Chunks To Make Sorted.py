"""
Function Name: max_chunks_to_sorted

Problem Summary:
----------------
Given an integer array 'arr' representing a permutation of integers in the range [0, n - 1],
split the array into the largest number of chunks such that sorting each chunk and concatenating
the results will yield the sorted version of the array.

Parameters:
-----------
- arr (List[int]): The input array representing a permutation of integers.

Returns:
--------
- chunks (int): The largest number of chunks that can be made.

Example:
--------
Input: arr = [1, 0, 2, f3, 4]
Output: 4

Constraints:
------------
- 1 <= len(arr) <= 10
- 0 <= arr[i] < len(arr)
- All elements of arr are unique.

Idea:
-----
- Track the maximum value seen so far.
- When the maximum value equals the current index, a valid chunk can be formed.
"""
from collections import deque
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = deque()

        for i, d in enumerate(arr)
