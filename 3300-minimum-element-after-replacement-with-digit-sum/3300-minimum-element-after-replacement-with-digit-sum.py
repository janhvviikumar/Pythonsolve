class Solution:
    def minElement(self, nums: List[int]) -> int:
        n=[]
        for elem in nums:
            sum=0
            l=[int(x) for x in str(elem)]
            for i in range(len(l)):
                sum+=l[i]
            n.append(sum)
        return min(n)
            


        