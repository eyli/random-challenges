# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find_or_count(node, k):
            if node is None:
                return (False, 0)

            left_found, left_value = find_or_count(node.left, k)
            if left_found:
                return left_found, left_value

            if left_value == k - 1:
                return True, node.val

            right_found, right_value = find_or_count(node.right, k - left_value - 1)
            if right_found:
                return right_found, right_value

            return False, left_value + 1 + right_value

        return find_or_count(root, k)[1]
