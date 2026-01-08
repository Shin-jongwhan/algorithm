class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lsM_zr = []
        for i in range(0, len(matrix)) : 
            for j in range(0, len(matrix[i])) : 
                if matrix[i][j] == 0 : 
                    lsM_zr.append([i, j])

        #print(lsM_zr)
        for i in range(0, len(lsM_zr)) : 
            #print(lsM_zr[i])
            matrix[lsM_zr[i][0]] = [0] * len(matrix[lsM_zr[i][0]])
            for j in range(0, len(matrix)) : 
                matrix[j][lsM_zr[i][1]] = 0

        #print(matrix)