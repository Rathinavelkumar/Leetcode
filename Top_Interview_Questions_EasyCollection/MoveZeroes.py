class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp1, temp2 = [], []
        for each in nums:
            if each==0:
                temp1.append(each)
            else:
                temp2.append(each)

        nums[:] = temp2 + temp1
        
        return nums