class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        res = []
        j = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
               res.append(i - j + 1)
               j = i + 1
        return res


            
            
