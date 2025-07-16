class Solution:
    def customSortString(self, order: str, s: str) -> str:
        pres=[]
        check=list(s)
        for i in s:
            if i in order:
                pres.append(i)
                check.remove(i)
        pres=sorted(pres,key=lambda x:order.index(x))
        return (''.join(pres)+''.join(check)) 