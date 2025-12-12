class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        op=[]
        ans=[]
        for i in range(len(nums)):
            if nums[i] not in op:
                op.append(nums[i])
            else:
                ans.append(nums[i])
        return ans

           
        