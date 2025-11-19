class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        temp=original
        i=0
        while i<len(nums):
            if nums[i]==temp:
                temp*=2
                i=0
            else:
                i+=1
        return temp