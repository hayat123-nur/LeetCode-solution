class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: i"""
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

        
        

        