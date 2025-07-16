class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(list(filter(lambda x:nums.count(x)==1,nums)))
        