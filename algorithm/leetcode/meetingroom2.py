# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
from functools import cmp_to_key

def mycompare(item1, item2):
    if item1.start!= item2.start:
        return item1.start - item2.start
    else:
        return item1.end - item2.end

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return len(intervals)
        intervals = sorted(intervals, key=cmp_to_key(mycompare))
        maxroom = 1
        endtime = [intervals[0].end]
        for i in range(1, len(intervals)):
            j = 0
            print(endtime, intervals[i].start, intervals[i].end, j)
            while j < len(endtime):
                #remove all early ones
                if intervals[i].start >= endtime[j]:
                    endtime.remove(endtime[j])
                else:
                    j = j+1
                
            endtime.append(intervals[i].end)
            if len(endtime) > maxroom:
                maxroom = len(endtime)
            
        return maxroom
         
        
        
print(Solution().minMeetingRooms([Interval(0, 30), Interval(5, 10),Interval(15, 20)]))