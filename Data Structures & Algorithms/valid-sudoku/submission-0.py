class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen=set()
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                   continue
                if num in seen:
                   return False
                else:
                    seen.add(num)
       
        for j in range(len(board)):
            seen=set()
            for i in range(len(board)):
                num=board[i][j]
                if num ==".":
                    continue
                if num in seen:
                    return False
                else:
                    seen.add(num)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen=set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        num = board[r][c]
                        if num ==".":
                            continue
                        if num in seen:
                            return False
                        else:
                            seen.add(num)
        return True