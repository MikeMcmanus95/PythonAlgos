'''
Leetcode #136: Single Number
https://leetcode.com/problems/single-number/
Time: O(n) | Space: O(1)

Additional reading: https://www.educative.io/courses/grokking-the-coding-interview/gk20xz4VwpG
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a
