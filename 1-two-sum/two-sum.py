class Solution:
    def twoSum(self,l,t):
        res=[]
        for a in range(len(l)):
            for b in range(len(l)):
                if a!=b:
                    if l[a]+l[b]==t:
                        if a not in res and b not in res:
                            res.append(a)
                            res.append(b)
        return res