class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for elem in nums:
            if (elem%3)==1:
                count+=1
            if (elem%3)==2:
                count+=1
        return count
        