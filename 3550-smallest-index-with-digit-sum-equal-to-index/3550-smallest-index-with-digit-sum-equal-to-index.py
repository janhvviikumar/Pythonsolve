class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ans=[]
        for i in range(len(nums)):
            b=list(str(nums[i]))
            sum=0
            for j in range(len(b)):
                sum+=int(b[j])
            if sum==i:
                ans.append(1)
                return i
                break
            else:
                ans.append(0)
        if 1 not in ans:
            return -1
           

        