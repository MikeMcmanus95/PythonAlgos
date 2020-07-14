'''
Leetcode #1: Two Sum
https://leetcode.com/problems/two-sum/
Time: O(n) | Space: O(n)
'''

from typing import List


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


def test_twoSum():
    sol = Solution()
    assert sol.twoSum([1, 2, 3, 5], 8) == [2, 3], "Should be [2,3]"


if __name__ == '__main__':
    test_twoSum()
    print("Everything passed!")
