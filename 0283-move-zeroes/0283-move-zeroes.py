class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        for elem in nums:
            if elem!=0:
                l.append(elem)
        for i in range(len(l)):
            nums[i]=l[i]
        for i in range(len(l),len(nums)):
            nums[i]=0

        
