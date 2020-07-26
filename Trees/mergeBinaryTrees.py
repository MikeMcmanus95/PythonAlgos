'''
Leetcode #617: Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/
Time: O(n) | Space: O(d) | d = depth of tree
'''
import TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2

        if t2 == None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
