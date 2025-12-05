class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count_left=0
        op=0
        for i in range(len(nums)-1):
            count_left+=nums[i]
            count_right=0
            for j in range(i+1,len(nums)):
                count_right+=nums[j]
            if (count_right-count_left)%2==0:
                op+=1
        return op
                