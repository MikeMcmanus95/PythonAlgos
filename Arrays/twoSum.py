'''
Leetcode #1: Two Sum
https://leetcode.com/problems/two-sum/
Time: O(n) | Space: O(n)
'''


class Solution:
  # Two Pass Approach
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freqCounter = {}
        for i in range(len(nums)):
            freqCounter[nums[i]] = i
        for i in range(len(nums)):
            firstNum = nums[i]
            secondNum = target - firstNum
            if secondNum in freqCounter and freqCounter[secondNum] != i:
                return [i, freqCounter[secondNum]]
        return [-1, -1]

  # One Pass Approach
    def twoSumOnePass(self, nums: List[int], target: int) -> List[int]:
        freqCounter = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in freqCounter:
                return [i, freqCounter[complement]]
            freqCounter[nums[i]] = i
        return [-1, -1]
