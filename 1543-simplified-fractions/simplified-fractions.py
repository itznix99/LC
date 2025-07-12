class Solution(object):
    def simplifiedFractions(self, n):
        def gcd(a,b):
            res=1
            if min(a,b)==2 and a%2==0 and b%2==0:
                res=2
            else:
                for i in range(2,min(a,b)+1):
                    if a%i==0 and b%i==0:
                        res=i
            return res
        
        if n==1:
            return []
        else:
            final=[]
            i,j=1,2
            while (j<=n):
                if i>=j:
                    j+=1
                    i=1
                else:
                    if gcd(i,j)==1:
                        final.append(str(i)+'/'+str(j))
                    i+=1
            return sorted(final,key=lambda x:[int(x.split('/')[0]),int(x.split('/')[1])])
        