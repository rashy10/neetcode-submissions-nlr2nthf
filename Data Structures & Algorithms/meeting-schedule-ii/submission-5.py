"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # intervals.sort()

        intervals.sort(key = lambda i:i.start)
        heap=[]

        for i in intervals:
            s , e = i.start,i.end

            if heap and heap[0] <= s:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
        return len(heap)

