class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        row=len(mat)
        column=len(mat[0])
        for _ in range(4):
            if mat==target:
                return True

            for i in range(row):
                for j in range(i+1,row):
                   mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for rows in mat:
              rows.reverse()
            
        return False