class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m1=min(nums)
        m2=max(nums)
        ans=[]
        for i in range(m1,m2+1):
            if i not in nums:
                ans.append(i)
        return ans
        