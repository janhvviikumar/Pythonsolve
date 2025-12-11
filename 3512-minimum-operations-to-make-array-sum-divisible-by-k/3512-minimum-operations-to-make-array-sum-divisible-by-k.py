class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum=0
        count=0
        for elem in nums:
            sum+=elem
        if sum<k:
            count+=sum
        elif sum%k==0:
            count+=0
        else:
            m=max(nums)
            count+=(sum%k)
        return count

        