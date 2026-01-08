class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ls = [[1]]
        if numRows == 1 : 
            return ls
        elif numRows == 2 : 
            ls.append([1,1])
            return ls
        else : 
            ls.append([1,1])

        for i in range(2, numRows) : 
            ls.append([0] * (i + 1))
            ls[i][0] = 1
            ls[i][-1] = 1
            for j in range(1, len(ls[i]) - 1) : 
                ls[i][j] = ls[i - 1][j - 1] + ls[i - 1][j]

        return ls