class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        l=[]
        if low%2!=0 or high%2!=0:
            count+=1
        a=(high-low)//2
        op=a+count  
        return op
        """for i in range(low,high+1):
            if i%2!=0:
                count+=1
        return count"""