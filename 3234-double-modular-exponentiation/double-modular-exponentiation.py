class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        check=[]
        for i in range(len(variables)):
            y=pow(pow(variables[i][0]%10,variables[i][1])%10,variables[i][2])
            print(y)
            if y%(variables[i][3])==target:
                check.append(i)
        return check
