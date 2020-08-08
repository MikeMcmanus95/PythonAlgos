'''
Leetcode #238: Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Time: O(n) | Space: O(1)
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultArr = [None for num in nums]
        resultArr[0] = 1
        product = 1
        for i in range(1, len(nums)):
            resultArr[i] = resultArr[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -2, -1):
            resultArr[i + 1] *= product
            product = nums[i + 1] * product
        return resultArr
