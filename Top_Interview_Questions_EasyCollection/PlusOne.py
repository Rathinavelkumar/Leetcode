class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result =  int(''.join( [ str(each) for each in digits ] )) + 1
        return list(str(result))