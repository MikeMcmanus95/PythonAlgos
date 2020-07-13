'''
Leetcode #1: Two Sum
https://leetcode.com/problems/two-sum/
Time: O(n) | Space: O(n)
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freqCounter = {}
        for i in range(len(nums)):
            freqCounter[nums[i]] = i
        for i in range(len(nums)):
            firstNum = nums[i]
            secondNum = target - firstNum
            if secondNum in freqCounter and freqCounter[secondNum] != i:
                return [i, freqCounter[secondNum]]
        return [0, 0]
