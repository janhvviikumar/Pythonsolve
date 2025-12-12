class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        sum=0
        for i in range(len(nums)):
            start=max(0,i-nums[i])
            end=i
            for j in range(start,end+1):
                sum+=nums[j]
        return sum

        