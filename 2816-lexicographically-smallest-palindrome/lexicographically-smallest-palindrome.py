class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l=list(s)
        for i in range(len(l)):
            if l[i]!=l[len(l)-i-1]:
                l[i]=min(l[i],l[len(l)-i-1])
        return ''.join(l)