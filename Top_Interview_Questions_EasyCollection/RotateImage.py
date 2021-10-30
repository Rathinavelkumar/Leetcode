class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        result=[]
        for i in range(len(matrix)):
            temp=[]
            for j in range(len(matrix)-1,-1,-1):
                temp.append(matrix[j][i])
            result.append(temp)
        matrix[:] = result
        return matrix