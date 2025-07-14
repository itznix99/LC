class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        res=[]
        for i in range(len(cost)):
            res.append(min(cost[:i+1]))
        return res