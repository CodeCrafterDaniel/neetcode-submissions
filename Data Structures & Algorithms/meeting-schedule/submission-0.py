"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        acts = []
        for i in intervals:
            acts.append((i.start, 1))
            acts.append((i.end, -1))

        acts.sort(key=lambda x: (x[0], x[1]))
        cur = 0
        for act in acts:
            cur += act[1]
            if cur > 1:
                return False
        return True
            