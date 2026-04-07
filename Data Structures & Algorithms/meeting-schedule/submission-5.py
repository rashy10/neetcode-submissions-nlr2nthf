"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        if intervals ==[]:
            return True
        res = []
        res =[intervals[0]]
        for i in intervals[1:]:
         
            if i.start< res[-1].end:
                return False
            else:
                res.append(i)
        return len(res)==len(intervals)

