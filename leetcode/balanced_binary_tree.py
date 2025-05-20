# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root)[0]

    def isBalancedHelper(self, root):
        if root is None:
            return (True, 0)

        left_balanced, left_height = self.isBalancedHelper(root.left)
        if not left_balanced:
            return (False, -1) # Height doesn't matter if not balanced.
        right_balanced, right_height = self.isBalancedHelper(root.right)

        is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return (is_balanced, max(left_height, right_height) + 1)
