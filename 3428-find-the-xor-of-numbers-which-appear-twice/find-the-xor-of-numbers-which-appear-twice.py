class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res=0
        for i in set(nums):
            if nums.count(i)==2:
                res^=i
        return res