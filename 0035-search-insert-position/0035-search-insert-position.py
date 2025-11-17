class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        i=0
        while i<len(nums):
            if nums[i]==target:
                return i
                break
            elif target<nums[i]:
                return i
                break
            else:
                i+=1
        if len(nums)==i:
            return i