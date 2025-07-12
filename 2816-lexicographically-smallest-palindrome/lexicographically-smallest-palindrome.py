class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l=list(s)
        for i in range(len(l)//2):
            if l[i]!=l[len(l)-i-1]:
                x=min(l[i],l[len(l)-i-1])
                if l[i]<l[len(l)-i-1]:
                    l[len(l)-i-1]=x
                else:
                    l[i]=x
        return ''.join(l)