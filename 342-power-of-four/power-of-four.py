class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if (n>0 and 4**(int(log(n,4)))==n):
            return True
        return False