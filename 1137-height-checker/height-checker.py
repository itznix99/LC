class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count,check=0,sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=check[i]:
                count+=1
        return count