class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row=len(matrix)
        column=len(matrix[0])
        transpose=[]
        for i in range(column):
            new_row=[]
            for j in range (row):
                new_row.append(matrix[j][i])
            transpose.append(new_row)
        return transpose