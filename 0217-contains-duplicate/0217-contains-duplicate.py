class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=len(nums)
        c=set(nums)
        b=len(c)
        if a==b:
            return False
        else:
            return True