class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count=0
        for i in set(s):
            if (i in t):
                if (s.count(i)>t.count(i)):
                    count+=(s.count(i)-t.count(i))
                    print(i)
            else:
                count+=s.count(i)
        return count