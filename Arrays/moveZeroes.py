'''
Leetcode #283: Move Zeroes
https://leetcode.com/problems/move-zeroes/
O(n) Time | O(1) Space
'''


'''
Input: [0,1,0,3,12]

Output: [1,3,12,0,0]

Approach:
 -Loop over array
 -Keep track of lastNonZeroElementIdx
 -When reaching a number that is a non zero, swap it with LNZE + 1, increment LNZE
 -Continue until loop terminates
'''




from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZeroElementIdx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                self.swap(i, lastNonZeroElementIdx, nums)
                lastNonZeroElementIdx += 1

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]
