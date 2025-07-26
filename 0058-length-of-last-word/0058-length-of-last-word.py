class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       a=s.strip().split(" ")
       b=len(a[-1])
       return b