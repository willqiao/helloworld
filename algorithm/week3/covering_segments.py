# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    
    segments = sorted(segments)
#     print(segments)
    
    index = 0
    start, end = segments[0][0],segments[0][1]
    
    while index + 1 < len(segments):
        nextStart = segments[index+1][0]
        if nextStart > end:
            points.append(end)
            start = nextStart
            end =  segments[index+1][1]
            index +=1            
        else:
            start = max(start, nextStart)
            end = min(end, segments[index+1][1])
            index +=1
    
    
    if len(points) == 0 or points[len(points)-1] != end:
        points.append(end)
        
        
    
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
#     n = 8
#     data = [4,7,1,3,2,5,5,6,2,7,3,5,6,9,10,11]
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#     print(segments)
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
