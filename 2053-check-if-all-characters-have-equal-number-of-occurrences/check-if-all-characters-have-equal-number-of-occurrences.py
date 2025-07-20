class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        check=s.count(s[0])
        for i in set(s[1:]):
            if s.count(i)!=check:
                return False
        return True