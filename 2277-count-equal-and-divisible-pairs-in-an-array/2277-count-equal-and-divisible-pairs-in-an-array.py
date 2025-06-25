class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # a=[i,j]
        # print'nums' if nums[i]==nums[j] and (i*j)/k else print'no pair exist' 
        n=len(nums)
        a=0
        for i in range(n):
            for j in range(i+1,n):
                if (i*j)%k==0 and nums[i]==nums[j]:
                    a+=1
        return a