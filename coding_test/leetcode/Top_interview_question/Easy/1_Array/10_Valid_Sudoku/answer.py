class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def validation(ls) : 
            if len(ls) == len(set(ls)) : 
                return True
            else : 
                return False


        cols = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        blCheck = True

        # 1. 먼저 col * row에 중복되는 숫자가 있으면 안 된다. 
        for col in cols : 
            lsTmp = []
            for row in rows : 
                lsTmp = [board[i][j] for i in col for j in row if board[i][j] != '.']
                #print(lsTmp)
                blCheck = validation(lsTmp)
                if blCheck == False : 
                    return blCheck
        print("1", blCheck)

        # 2. 한 row에 중복되는 숫자가 있으면 안 된다.
        # 3. 한 col에 중복되는 숫자가 있으면 안 된다.
        cols = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        rows = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        lsCol = []
        lsRow = []
        for i in cols :
            for j in rows : 
                if board[i][j] != '.' : 
                    lsRow.append(board[i][j])
                if board[j][i] != '.' : 
                    lsCol.append(board[j][i])
            blCheck = validation(lsRow)
            if blCheck == False : 
                return blCheck
            blCheck = validation(lsCol)
            if blCheck == False : 
                return blCheck
            lsRow = []
            lsCol = []

        print("2", blCheck)
        
        return blCheck