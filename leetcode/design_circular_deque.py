# https://leetcode.com/problems/design-circular-deque/description/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.count = 0
        self.capacity = k
        self.front = None
        self.last = None

    def insertFront(self, value: int) -> bool:
        if self.count == self.capacity:
            return False

        new_node = Node(value)
        if not self.front:
            self.last = new_node
        else:
            self.front.prev = new_node
            new_node.next = self.front
        self.front = new_node
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        new_node = Node(value)
        if not self.last:
            self.front = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
        self.last = new_node
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if not self.front:
            return False

        if self.count == 1:
            self.front = None
            self.last = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if not self.last:
            return False
        if self.count == 1:
            self.front = None
            self.last = None
        else:
            self.last = self.last.prev
            self.last.next = None
        self.count -= 1
        return True

    def getFront(self) -> int:
        if not self.front:
            return -1

        return self.front.val

    def getRear(self) -> int:
        if not self.last:
            return -1

        return self.last.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
