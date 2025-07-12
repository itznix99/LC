class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if i//10==0:
                res.append(i)
            else:
                for j in str(i):
                    res.append(int(j))
        return res
