class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        newset=set(nums)
        n=len(newset)
        lists=list(newset)
        if n<3:
           return max(lists)
        lists.sort(reverse=True)
        return lists[2]


        