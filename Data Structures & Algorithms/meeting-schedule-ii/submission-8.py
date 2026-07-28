"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        end_times = []

        for i in range(len(intervals)):
            if end_times and intervals[i].start >= end_times[0]:
                heapq.heappop(end_times)
            heapq.heappush(end_times, intervals[i].end)
             
        return len(end_times)