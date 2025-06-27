class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # for num in nums:
        #     if nums.count(num)>1:
        #         return True
        #     else:
        #         return False
        return len(nums)!=len(set(nums))