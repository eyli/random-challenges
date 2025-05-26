# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        # Each element is a tuple: (value, current_min)
        self.stack = []

    def push(self, val: int) -> None:
        current_min = val if not self.stack else min(val, self.getMin())
        self.stack.append((val, current_min))

    def pop(self) -> int:
        if self.stack:
            self.stack.pop()[0]

    def top(self) -> int | None:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int | None:
        return self.stack[-1][1] if self.stack else None
