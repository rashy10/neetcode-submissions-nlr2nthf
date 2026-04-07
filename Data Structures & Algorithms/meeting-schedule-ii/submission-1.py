"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if intervals == []:
            return 0
        intervals.sort(key = lambda i:i.end)

        i = 0
        res=[0]
        while intervals:
            found = False
            for j in range(len(res)):
                if res[j] <= intervals[0].start:  
                    res[j] = intervals[0].end 
                    intervals.pop(0)  
                    found = True
                    break  
            if not found:  
                res.append(intervals[0].end)
                intervals.pop(0)
                i += 1
        return len(res)

        
        