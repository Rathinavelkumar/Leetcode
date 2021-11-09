class Solution:
    def countAndSay(self, n: int) -> str:
        res=[]
        if n>0:
            res=[1]
            while n>1:
                n=n-1
                res = self.calculate_count(res)
        return("".join([ str(each) for each in res]))
    
    def calculate_count(self, arr):
        counter=0
        result=[]
        for j, each in enumerate(arr):
            counter=counter+1
            if j==len(arr)-1:
                result.extend([counter, each])
            elif arr[j+1]==each:
                continue
            else:
                result.extend([counter, each])
                counter=0
        return result