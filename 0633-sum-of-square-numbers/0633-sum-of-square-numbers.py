class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j=0
        while j*j<=c:
           j+=1
        j-=1
        i=0
        while i <= j:
            total=i*i + j*j
            if total==c:
               return True
            elif total<c:
               i+=1
            else:
               j-=1
        return False