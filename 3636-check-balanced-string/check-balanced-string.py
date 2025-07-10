class Solution:
    def isBalanced(self, nums: str) -> bool:
        l=[0,0]
        for i in range(len(nums)):
            if i%2==0:
                l[0]+=int(nums[i])
            else:
                l[1]+=int(nums[i])
        return l[0]==l[1]