# https://leetcode.com/problems/my-calendar-ii/

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 1
        self.left = None
        self.right = None

class MyCalendarTwo:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        else:
            return self.insert(start, end, self.root)

    def insertable(self, start, end, node):
        if not node:
            return True

        if node.start >= end:
            return self.insertable(start, end, node.left)
        elif node.end <= start:
            return self.insertable(start, end, node.right)
        else:
            if node.count >= 2:
                return False
            else:
                left = min(start, node.start)
                overlap_left = max(start, node.start)
                overlap_right = min(end, node.end)
                right = max(end, node.end)

                return (
                    self.insertable(left, overlap_left, node.left) and
                    self.insertable(overlap_right, right, node.right)
                )

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
            if node.count >= 2:
                return False
            else:
                new_start = min(start, node.start)
                overlap_start = max(start, node.start)
                overlap_end = min(end, node.end)
                new_end = max(end, node.end)

                insertable = (
                    self.insertable(new_start, overlap_start, node.left) and
                    self.insertable(overlap_end, new_end, node.right)
                )
                if insertable:
                    node.count += 1
                    node.start = overlap_start
                    node.end = overlap_end
                    self.insert(new_start, overlap_start, node)
                    self.insert(overlap_end, new_end, node)
                return insertable
