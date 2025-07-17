class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        a=[]
        maxs_point=0
        for i in points:
            a.append(i[0])
        a.sort()
        for i in range(1,len(a)):
            maxs_point=max(maxs_point,a[i]- a[i-1])
        return maxs_point