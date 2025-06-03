# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root is None:
            return output

        nodes_to_visit = [(root, 0)]
        while nodes_to_visit:
            node, depth = nodes_to_visit.pop()
            if depth == len(output):
                output.append(node.val)
            if node.left is not None:
                nodes_to_visit.append((node.left, depth+1))
            if node.right is not None:
                nodes_to_visit.append((node.right, depth+1))
        return output
