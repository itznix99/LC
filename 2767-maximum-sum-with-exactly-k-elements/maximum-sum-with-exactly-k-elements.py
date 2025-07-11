class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score=0
        while k>0:
            score+=max(nums)
            nums[nums.index(max(nums))]+=1
            k-=1
        return score