# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    def __str__(self):
        return str(self.start) + ',' + str(self.end)
    
    def __repr__(self):
        return str(self.start) + ',' + str(self.end)

def getStart(interval):
    return interval.start

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        intervals = sorted(intervals, key=getStart)
        currentX = intervals[0].start
        currentY = intervals[0].end
        for i in range(len(intervals)):
            if intervals[i].start <= currentY:
                currentY =  intervals[i].end
            elif intervals[i].start > currentY:
                result.append(Interval(currentX, currentY))
                currentX = intervals[i].start
                currentY = intervals[i].end
        result.append(Interval(currentX, currentY))
        return result


print(Solution().merge([Interval(1,3), Interval(8,10), Interval(2,6),Interval(9,18)]))