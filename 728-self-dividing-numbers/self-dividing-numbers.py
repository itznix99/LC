class Solution(object):
    def selfDividingNumbers(self, left, right):
        res=[]
        for i in range(left,right+1):
            if '0' in str(i):
                continue
            elif len(list(filter(lambda x:i%int(x)==0,list(str(i)))))==len(str(i)):
                res.append(i)
        return res        