# https://leetcode.com/problems/find-median-from-data-stream/

from heapq import *

class MedianFinder:
    def __init__(self):
        self.lowers = [] # all negated to make it a max heap
        self.uppers = []

    def addNum(self, num: int) -> None:
        if not self.lowers or num <= -self.lowers[0]:
            heappush(self.lowers, -num)
        else:
            heappush(self.uppers, num)

        if len(self.uppers) - len(self.lowers) == 2:
            heappush(self.lowers, -heappop(self.uppers))
        if len(self.lowers) - len(self.uppers) == 2:
            heappush(self.uppers, -heappop(self.lowers))

    def findMedian(self) -> float:
        if len(self.lowers) > len(self.uppers):
            return -self.lowers[0]
        elif len(self.uppers) > len(self.lowers):
            return self.uppers[0]
        else:
            return (self.uppers[0] - self.lowers[0]) / 2
