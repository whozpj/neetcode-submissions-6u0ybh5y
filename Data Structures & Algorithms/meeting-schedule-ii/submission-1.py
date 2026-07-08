"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        

        starts = []
        ends = []

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)

        starts.sort()
        ends.sort()

        result = 0
        count = 0
        s = 0
        e = 0

        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            result = max(result, count)

        return result