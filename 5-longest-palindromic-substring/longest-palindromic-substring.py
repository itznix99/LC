class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxs,maxl=0,0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if i!=j:
                    s1=s[i:j]
                    if s1==s1[-1::-1] and len(s1)>maxl:
                        maxs=s1
                        maxl=len(s1)
        return maxs