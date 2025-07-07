# https://leetcode.com/problems/task-scheduler/

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        next_available = {}

        current_time = 0
        while task_counts:
            next_task = None
            highest_task_count = 0

            for task, count in task_counts.items():
                if next_available.get(task, 0) <= current_time:
                    if task_counts[task] > highest_task_count:
                        next_task = task
                        highest_task_count = task_counts[task]

            if not next_task:
                next_task, next_time = min(next_available.items(), key=lambda x: x[1])
                current_time = next_time

            current_time += 1
            next_available[next_task] = current_time + n
            task_counts[next_task] -= 1
            if task_counts[next_task] == 0:
                del(task_counts[next_task])
                del(next_available[next_task])

        return current_time
