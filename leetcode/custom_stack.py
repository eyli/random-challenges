# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize
        self.current_increment = 0

    def push(self, x: int) -> None:
        if len(self.stack) == self.max_size:
            return

        if self.stack:
            value, increment = self.stack[-1]
            self.stack[-1] = (value, increment+self.current_increment)
        self.current_increment = 0

        self.stack.append((x, 0))


    def pop(self) -> int:
        if not self.stack:
            return -1

        value, additional_increment = self.stack.pop()
        self.current_increment += additional_increment
        return value + self.current_increment

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return

        index_to_increment = min(k, len(self.stack)) - 1
        value, increment = self.stack[index_to_increment]
        self.stack[index_to_increment] = (value, increment+val)
