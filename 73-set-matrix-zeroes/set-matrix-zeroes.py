class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = [-1] * len(matrix)
        col = [-1] * len(matrix[0])
        for i in range(len(rows)):
            for j in range(len(col)):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    col[j] = 0
        for i in range(len(rows)):
           if rows[i] == 0:
            for value in range(len(col)):
                matrix[i][value] = 0

       
        for i in range(len(col)):
           if col[i] == 0:
            for value in range(len(rows)):
                matrix[value][i] = 0
        
        return matrix
