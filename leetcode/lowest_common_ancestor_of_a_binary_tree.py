# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        nodes_found = {'p': False, 'q': False}
        result = self._helper(root, p, q, nodes_found)
        if nodes_found['p'] and nodes_found['q']:
            return result
        else:
            return None

    def _helper(self, node, p, q, nodes_found):
        if not node:
            return None

        left = self._helper(node.left, p, q, nodes_found)
        right = self._helper(node.right, p, q, nodes_found)

        if node == p:
            nodes_found['p'] = True
            return node
        elif node == q:
            nodes_found['q'] = True
            return node
        else:
            if left is not None and right is not None:
                return node
            elif left is None:
                return right
            else:
                return left
