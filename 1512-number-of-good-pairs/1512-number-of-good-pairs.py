class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i=0
        count=0
        while i<len(nums):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            i+=1
        return count
        