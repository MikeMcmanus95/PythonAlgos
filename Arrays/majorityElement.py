from typing import List


class Solution:
    # Approach 1: Hash Table and Loop. O(n) Time | O(n) Space
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {}
        for num in nums:
            numCount[num] = 1 if num not in numCount else numCount[num] + 1
            if numCount[num] > len(nums) / 2:
                return num

    # Approach 2: Boyer-Moore Voting Algorithm. O(n) Time | O(1) Space
    def majorityElementMoores(self, nums: List[int]) -> int:
        count = 1
        majorityElement = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num != majorityElement:
                count -= 1
            else:
                count += 1
            if count == 0:
                majorityElement = num
                count = 1
        return majorityElement
