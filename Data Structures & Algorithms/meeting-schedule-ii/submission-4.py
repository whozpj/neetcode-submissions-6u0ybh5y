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


        count = 0
        result = 0

        s_Index = 0
        e_Index = 0

        while s_Index < len(starts):
            if starts[s_Index] < ends[e_Index]:
                count += 1
                s_Index += 1
            else:
                count -= 1
                e_Index += 1
            result = max(count, result)


        return result