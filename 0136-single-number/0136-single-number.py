class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=0
        for elem in nums:
            if nums.count(elem)==1:
                return elem
