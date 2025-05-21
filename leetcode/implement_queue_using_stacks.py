# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if self.empty():
            raise Exception("Queue is empty and has no items to pop.")

        self._flush_push_stack()

        return self.pop_stack.pop()

    def peek(self) -> int:
        if self.empty():
            raise Exception("Queue is empty and has no items to peek.")

        self._flush_push_stack()

        return self.pop_stack[-1]

    def _flush_push_stack(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())

    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack
