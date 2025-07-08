# https://leetcode.com/problems/lru-cache/

class LRUCache:
    class Node:
        def __init__(self, key, value, prev=None, nxt=None):
            self.key = key
            self.value = value
            self.prev = prev
            self.nxt = nxt

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.head = None
        self.tail = None

    def _remove(self, node):
        if node.prev:
            node.prev.nxt = node.nxt
        else:
            self.head = node.nxt
        if node.nxt:
            node.nxt.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = None
        node.nxt = None

    def _append_to_tail(self, node):
        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.nxt = node
            self.tail = node

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]
        if node is not self.tail:
            self._remove(node)
            self._append_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.value = value
            if node is not self.tail:
                self._remove(node)
                self._append_to_tail(node)
        else:
            new_node = self.Node(key, value)
            self.store[key] = new_node
            self._append_to_tail(new_node)

            if len(self.store) > self.capacity:
                lru = self.head
                self._remove(lru)
                del self.store[lru.key]
