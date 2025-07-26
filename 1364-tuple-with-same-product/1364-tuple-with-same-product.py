class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
    
        count=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod=nums[i]*nums[j]
                count[prod]+=1
        result=0
        for c in count.values():
            if c>1:
                result+=c*(c-1)//2
        return result * 8
        


        
