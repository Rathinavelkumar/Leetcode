class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp not in result:
                result[nums[i]] = i
            else:
                return [result[temp],i]