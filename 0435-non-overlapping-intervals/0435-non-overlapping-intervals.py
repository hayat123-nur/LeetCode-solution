class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        prevint=intervals[0][1]
        for interval in intervals[1:]:
            if prevint<=interval[0]:
                prevint=interval[1]
            else:
                prevint=min(prevint,interval[1])
                count+=1
        return count

            