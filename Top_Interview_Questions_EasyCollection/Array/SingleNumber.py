class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=[]
        for each in nums:
            if each in result:
                result.remove(each)
            else:
                result.append(each)
        return result[0]