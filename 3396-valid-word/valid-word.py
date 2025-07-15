class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        if (not word.isalnum()):
            return False
        vow,con=0,0
        for i in set(word.lower()):
            if i.isalpha():
                if i in 'aeiou':
                    vow+=1
                else:
                    con+=1
            if vow>=1 and con>=1:
                return True
        return False
            