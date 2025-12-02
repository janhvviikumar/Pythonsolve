class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        op=[]
        for i in range(len(candies)):
            temp=candies[i]+extraCandies
            if (temp==max(candies)) or (temp>max(candies)):
                op.append(True)
            else:
                op.append(False)
        return op