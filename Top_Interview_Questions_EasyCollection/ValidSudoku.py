class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag=True
        
        for i in range(len(board)):
            length, breadth, square = [], [], []
            
            for j in range(len(board)):
                
                #List creation with numeric values - length wise
                if board[i][j].isdigit(): 
                    length.append(board[i][j])
                #List creation with numeric values - breadth wise
                if board[j][i].isdigit(): 
                    breadth.append(board[j][i])
                #List creation with numeric values - 3*3 subarray
                a=((i//3)*3)+(j//3)
                b=((i%3)*3)+(j%3)
                if board[a][b].isdigit(): 
                    square.append(board[a][b])
            
            #Check whether the sub-list having any duplicate entries
            if len(length)!=len(set(length)) or len(breadth)!=len(set(breadth)) or len(square)!=len(set(square)):
                flag=False
                break
            
        return flag