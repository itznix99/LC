class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[[],[]]
        l1=set(nums1)
        l2=set(nums2)
        for i in l1:
            if i not in l2:
                res[0].append(i)
        for i in l2:
            if i not in l1:
                res[1].append(i)
        return res