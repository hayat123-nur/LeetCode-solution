class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:      
         a=[]
         b=[]
         c=[]
         for num in nums:
             if num%2==0:
                a.append(num)
             else:
                b.append(num)
         c.extend(a)
         c.extend(b)
         return c