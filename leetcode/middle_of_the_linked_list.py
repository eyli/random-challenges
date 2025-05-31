# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        hare = head
        while hare is not None:
            hare = hare.next
            if hare is None:
                return tortoise
            tortoise = tortoise.next
            hare = hare.next
        return tortoise
