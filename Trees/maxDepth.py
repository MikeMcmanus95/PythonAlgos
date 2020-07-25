'''
Leetcode #104: Maximum Depth of a Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Time: O(n) | Space: O(d) | d = depth of tree
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode, count: int = 0, maxCount: int = 0) -> int:
        if count > maxCount:
            maxCount = count
        if root == None:
            return maxCount
        return max(self.maxDepth(root.left, count + 1, maxCount), self.maxDepth(root.right, count + 1, maxCount))
