# https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        koala = head
        if koala is None:
            return False

        gazelle = head.next
        while gazelle:
            if koala == gazelle:
                return True

            koala = koala.next
            gazelle = gazelle.next
            if gazelle is None:
                return False
            gazelle = gazelle.next

        return False
