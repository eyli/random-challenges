# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        targets1 = self._target_nodes(edges1, k)
        targets2 = self._target_nodes(edges2, k-1)
        highest_target = max(targets2)
        return [val + highest_target for val in targets1]

    def _target_nodes(self, edges, k):
        edge_map = {}
        for edge in edges:
            node0_connections = edge_map.setdefault(edge[0], [])
            node1_connections = edge_map.setdefault(edge[1], [])

            node0_connections.append(edge[1])
            node1_connections.append(edge[0])

        output = []
        for node in range(len(edge_map)):
            seen = set()
            distance_traveled = 0
            nodes_to_traverse = deque([node])
            while distance_traveled <= k and nodes_to_traverse:
                for i in range(len(nodes_to_traverse)):
                    current_node = nodes_to_traverse.popleft()
                    seen.add(current_node)
                    for connection in edge_map[current_node]:
                        if connection not in seen:
                            nodes_to_traverse.append(connection)
                distance_traveled += 1
            output.append(len(seen))
        return output
