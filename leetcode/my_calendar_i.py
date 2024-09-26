# https://leetcode.com/problems/my-calendar-i

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        else:
            return self.insert(start, end, self.root)

    def insert(self, start, end, node):
        if node.start >= end:
            if node.left:
                return self.insert(start, end, node.left)
            else:
                node.left = Node(start, end)
                return True
        elif node.end <= start:
            if node.right:
                return self.insert(start, end, node.right)
            else:
                node.right = Node(start, end)
                return True
        else:
            return False
