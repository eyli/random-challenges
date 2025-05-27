# https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._is_valid_helper(root, None, None)

    def _is_valid_helper(self, root, lower_bound, upper_bound):
        if root is None:
            return True

        if lower_bound is not None and root.val <= lower_bound:
            return False
        if upper_bound is not None and root.val >= upper_bound:
            return False

        left_valid = self._is_valid_helper(root.left, lower_bound, root.val)
        return left_valid and self._is_valid_helper(root.right, root.val, upper_bound)
