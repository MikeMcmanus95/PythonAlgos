'''
Leetcode #561: Array Partition I
https://leetcode.com/problems/array-partition-i/
Time: O(n log(n)) | Space: O(1)
'''
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                maxSum += nums[i]
        return maxSum


def test_arrayPairSum():
    sol = Solution()
    assert sol.arrayPairSum([1, 4, 3, 2]) == 4, "Should be 4"


if __name__ == '__main__':
    test_arrayPairSum()
    print('Everything passed!')
