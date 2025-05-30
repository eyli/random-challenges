# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        output = f"{root.val}({left})({right})"
        print(output)
        return output

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self._deserialize_node(data, 0)[0]

    # Returns the corresponding node, as well as the index where it ended when deserializing.
    def _deserialize_node(self, data, start):
        if start >= len(data) or data[start] == ")":
            return None, start

        i = start
        if data[i] == "-":
            i += 1
        while i < len(data) and data[i].isdigit():
            i += 1
        value = int(data[start:i])
        left, left_end_index = self._deserialize_node(data, i+1)
        right_start = left_end_index + 2
        right, right_end_index = self._deserialize_node(data, right_start)

        output_node = TreeNode(value)
        output_node.left = left
        output_node.right = right
        return output_node, right_end_index + 1
