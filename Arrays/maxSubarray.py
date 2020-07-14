'''
Leetcode #53: Maximum Subarray (Kadane's Algorithm)
https://leetcode.com/problems/maximum-subarray/
Time: O(n) | Space: O(1)
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        maxSum = currentSum
        for i in range(1, len(nums)):
            if currentSum + nums[i] > nums[i]:
                currentSum += nums[i]
            else:
                currentSum = nums[i]
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum


def test_maxSubArray():
    sol = Solution()
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "Should be 6"


if __name__ == '__main__':
    test_maxSubArray()
    print("Everything passed!")
