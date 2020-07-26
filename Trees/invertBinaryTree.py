'''
Leetcode #226: Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
Time: O(n) | Space: O(d) | d = depth
'''

import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
