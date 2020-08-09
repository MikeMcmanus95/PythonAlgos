'''
Leetcode #270: Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/
Time: O(H) | Space: O(1)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        val = root.val
        while root is not None:
            val = root.val
            closest = val if abs(val - target) < abs(closest - target) else closest
            root = root.left if val > target else root.right
        return closest
