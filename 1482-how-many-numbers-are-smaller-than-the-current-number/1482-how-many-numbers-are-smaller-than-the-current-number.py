class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        
        counts=0
        for i in nums:
            for j in nums:
                if i>j:
                   counts+=1
            a.append(counts)
            counts=0
        return a