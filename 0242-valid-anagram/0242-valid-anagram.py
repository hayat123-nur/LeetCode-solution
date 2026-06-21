class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        i=Counter(s)
        j=Counter(t)
        return i==j