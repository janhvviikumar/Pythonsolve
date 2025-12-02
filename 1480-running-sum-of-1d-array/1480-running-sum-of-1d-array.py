class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        op=[]
        for elem in nums:
            sum+=elem
            op.append(sum)
        return op
        