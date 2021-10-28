class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for each in nums1:
            if each in nums2:
                result.append(each)
                nums2.remove(each)

        return result