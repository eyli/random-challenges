# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.clone_graph_helper(node, {})

    def clone_graph_helper(self, node, nodes_seen):
        if node is None:
            return None
        if node.val in nodes_seen:
            return nodes_seen[node.val]

        node_copy = Node(node.val)
        nodes_seen[node.val] = node_copy
        for neighbor in node.neighbors:
            node_copy.neighbors.append(self.clone_graph_helper(neighbor, nodes_seen))

        return node_copy
