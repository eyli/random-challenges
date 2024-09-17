# https://leetcode.com/problems/task-scheduler-ii/

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        expirations = {}
        current_time = 0
        for task in tasks:
            task_expiration = expirations.get(task, 0)
            current_time = max(current_time, task_expiration) + 1
            expirations[task] = current_time + space

        return current_time
