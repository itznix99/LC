class Solution:
    def findGCD(self, nums: List[int]) -> int:
        gcd=1
        for i in range(2,min(nums)+1):
            if min(nums)%i==0 and max(nums)%i==0:
                gcd=i
        return gcd
        