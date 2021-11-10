class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)>0:
            temp=strs[0]
            result=""
            for i in range(len(temp)):
                search=temp[:i+1]
                for j in range(1,len(strs)):
                    if not strs[j].startswith(search):
                        break
                else:
                    if len(search)>len(result):
                        result=search
            return(result)
        else:
            return("")