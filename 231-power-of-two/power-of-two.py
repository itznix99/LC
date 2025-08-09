class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n<=0):
            return False
        if ((2**(int(log(n,2))))==n):
            return True
        return False