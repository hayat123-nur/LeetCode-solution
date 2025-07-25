class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
       
        row=len(mat)
        column=len(mat[0])
        result=[]
        for d in range(column+row -1):
            temp=[]
            if d < column:
                r=0
                c=d
            else:
                r=d-column+1
                c=column-1
            while r<row and c >= 0:
                temp.append(mat[r][c])
                r+=1
                c-=1
            if d%2 == 0:
                temp.reverse()
            result.extend(temp)
        return result
       