class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag=True

        for i in range(len(board)):
            length, breath, square = [], [], []   
            for j in range(len(board)):
                #List creation with numeric values - length wise
                if board[i][j].isdigit():
                    length.append(board[i][j])
                #List creation with numeric values - breath wise
                if board[j][i].isdigit():    
                    breath.append(board[j][i])
                #List creation with numeric values - 3*3 subarray
                a=((i//3)*3)+(j//3)
                b=((i%3)*3)+(j%3)
                if board[a][b].isdigit(): 
                    square.append(board[a][b])

            #Find the duplicate in ca
            if len(length)!=len(set(length)) or len(breath)!=len(set(breath)) or len(square)!=len(set(square)):
                flag=False
                break

        return flag