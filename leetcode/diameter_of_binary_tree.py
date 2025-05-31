# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self._diameter_helper(root)[0]

    # returns (diameter, height)
    def _diameter_helper(self, node):
        if node is None:
            return (0, 0)

        left_diameter, left_height = self._diameter_helper(node.left)
        right_diameter, right_height = self._diameter_helper(node.right)
        mid_diameter = left_height + right_height
        return (
            max(left_diameter, mid_diameter, right_diameter),
            max(left_height, right_height) + 1
        )
