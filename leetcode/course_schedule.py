# https://leetcode.com/problems/course-schedule/

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs_map = defaultdict(list)
        for prereq, course in prerequisites:
            prereqs_map[course].append(prereq)

        can_take = {}
        for i in range(numCourses):
            if not self.can_take_course(i, prereqs_map, can_take):
                return False
        return True

    def can_take_course(self, course, prereqs_map, can_take):
        if course not in prereqs_map:
            return True
        elif course in can_take:
            return can_take[course]
        else:
            can_take[course] = False
            for prereq in prereqs_map[course]:
                if not self.can_take_course(prereq, prereqs_map, can_take):
                    return False
            can_take[course] = True
            return True
