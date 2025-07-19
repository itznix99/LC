class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res=list(s)
        while True:
            x=s.find(part)
            if (x==-1):
                break
            del res[x:x+len(part)]
            s=''.join(res)
        return ''.join(res)