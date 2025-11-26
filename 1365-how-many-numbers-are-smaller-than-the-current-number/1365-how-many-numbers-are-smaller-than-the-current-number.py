class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=0
        ans=[]
        i=0
        while i<len(nums):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            ans.append(count)
            count=0
            i+=1
        return ans
                