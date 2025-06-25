# https://leetcode.com/problems/merge-k-sorted-lists/

from heapq import heappush, heappop
from random import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [] # Heap of (val, ListNode) tuples

        for list_head in lists:
            if list_head:
                heappush(heap, (list_head.val, random(), list_head))

        output_head = ListNode()
        tail = output_head
        while heap:
            val, _, list_node = heappop(heap)
            next_node = ListNode(val)
            tail.next = next_node
            tail = next_node
            if list_node.next:
                next_node = list_node.next
                heappush(heap, (next_node.val, random(), next_node))
        return output_head.next
