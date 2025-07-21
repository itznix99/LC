class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res=['a']
        word,i=['a'],0
        while (''.join(word)!=target):
            if word[i]!=target[i]:
                word[i]=chr(ord(word[i])+1)
            else:
                word.append('a')
                i+=1
            res.append(''.join(word))
        return res