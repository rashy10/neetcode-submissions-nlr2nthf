"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals==[]:
            return True
        intervals.sort(key = lambda x: x.start)
        prev = intervals[0].end

 
        for i in intervals[1:]:
            if i.start >= prev:
                prev = i.end
            else:
                return False
        return True
